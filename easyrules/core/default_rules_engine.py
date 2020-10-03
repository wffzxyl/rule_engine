# coding: utf-8
"""
Default RulesEngine implementation.
Rules are fired according to their natural order which is priority by default.
This implementation iterates over the sorted set of rules, evaluates the condition
of each rule and executes its actions if the condition evaluates to true.
"""

import traceback
from easyrules.api import Rule, Facts, Rules, RulesEngineParameters
from easyrules.utils import logger
from .abstract_rules_engine import AbstractRulesEngine


class DefaultRuleEngine(AbstractRulesEngine):
    def __init__(self, parameters: RulesEngineParameters = None):
        super(DefaultRuleEngine, self).__init__(parameters)

    def fire(self, rules: Rules, facts: Facts):
        self._trigger_listeners_before_fire(rules, facts)
        self._do_fire(rules, facts)
        self._trigger_listeners_after_fire(rules, facts)

    def _do_fire(self, rules: Rules, facts: Facts):
        if len(rules) == 0:
            logger.warning('No rules registered! Nothing to apply')
            return

        self._log_parameters()
        self._log_rules_and_facts(rules, facts)

        logger.debug("Rules evaluation started")
        for rule in rules:
            name = rule.name
            domain = rule.domain
            if not domain: continue
            priority = rule.priority
            if (priority > self._parameters.rule_priority_threshold):
                logger.debug('Rule priority threshold %s exceeded at rule %s with priority %s, next rules will be skipped' %
                             (self._parameters.rule_priority_threshold, name, priority))
                continue

            if not self.should_be_evaluated(rule, facts):
                logger.debug("Rule %s has been skipped before being evaluated" % name)
                continue

            evaluation_result = False
            try:
                evaluation_result = rule.evaluate(facts)
                if self._parameters.skip_on_first_applied_rule:
                    break
            except Exception as e:
                logger.error("Rule %s evaluated with error, %s" % (name, traceback.format_exc()))
                self._trigger_listeners_on_evaluate_error(rule, facts, e)
                if self._parameters.skip_on_first_non_triggered_rule:
                    logger.debug("Next rules will be skipped since parameter skip_on_first_non_triggered_rule is set")
                    break

            if evaluation_result:
                logger.debug("Rule %s triggered" % name)
                self._trigger_listeners_after_evaluate(rule, facts, True)
                try:
                    self._trigger_listeners_before_execute(rule, facts)
                    rule.execute(facts)
                    logger.debug("Rule %s performed successfully" % name)
                    self._trigger_listeners_on_success(rule, facts)
                    if self._parameters.skip_on_first_applied_rule:
                        print("Next rules will be skipped since parameter skip_on_first_applied_rule is set")
                        break
                except Exception as e:
                    logger.error("Rule %s executed with error, %s" % (name, traceback.format_exc()))
                    self._trigger_listeners_on_failure(rule, facts, e)
                    if self._parameters.skip_on_first_failed_rule:
                        print("Next rules will be skipped since parameter skip_on_first_failed_rule is set")
                        break
            else:
                logger.debug("Rule %s has been evaluated to False, it has not been executed" % name)
                self._trigger_listeners_after_evaluate(rule, facts, False)
                if self._parameters.skip_on_first_non_triggered_rule:
                    logger.debug("Next rules will be skipped since parameter skip_on_first_non_triggered_rule is set")
                    break

    def _log_parameters(self):
        logger.info('Parameters: %s' % self._parameters)

    def _log_rules_and_facts(self, rules: Rules, facts: Facts):
        logger.info('Registered rules:')
        for rule in rules:
            logger.info(rule)

        logger.info('Known facts:')
        for fact in facts:
            logger.info(fact)

    def check(self, rules: Rules, facts: Facts):
        self._trigger_listeners_before_fire(rules, facts)
        result = self.do_check(rules, facts)
        self._trigger_listeners_after_fire(rules, facts)
        return result

    def do_check(self, rules: Rules, facts: Facts):
        logger.debug('Checking rules')
        result = {}
        for rule in rules:
            if self.should_be_evaluated(rule, facts):
                result[rule.name] = rule.evaluate(facts)
        return result

    def _trigger_listeners_before_fire(self, rules: Rules, facts: Facts):
        for rule_engine_listener in self._rule_engine_listeners:
            rule_engine_listener.before_evaluate(rules, facts)

    def _trigger_listeners_after_fire(self, rules: Rules, facts: Facts):
        for rule_engine_listener in self._rule_engine_listeners:
            rule_engine_listener.after_evaluate(rules, facts)

    def should_be_evaluated(self, rule: Rule, facts: Facts):
        return self._trigger_listeners_before_evaluate(rule, facts)

    def _trigger_listeners_before_evaluate(self, rule: Rule, facts: Facts):
        for rule_listener in self._rule_listeners:
            if not rule_listener.before_evaluate(rule, facts):
                return False
        return True

    def _trigger_listeners_on_evaluate_error(self, rule: Rule, facts: Facts, exception: Exception):
        for rule_listener in self._rule_listeners:
            rule_listener.on_evaluation_error(rule, facts, exception)

    def _trigger_listeners_after_evaluate(self, rule: Rule, facts: Facts, evaluation_result: bool):
        for rule_listener in self._rule_listeners:
            rule_listener.after_evaluate(rule, facts, evaluation_result)

    def _trigger_listeners_before_execute(self, rule: Rule, facts: Facts):
        for rule_listener in self._rule_listeners:
            rule_listener.before_execute(rule, facts)

    def _trigger_listeners_on_success(self, rule: Rule, facts: Facts):
        for rule_listener in self._rule_listeners:
            rule_listener.on_success(rule, facts)

    def _trigger_listeners_on_failure(self, rule: Rule, facts: Facts, exception: Exception):
        for rule_listener in self._rule_listeners:
            rule_listener.on_failure(rule, facts, exception)
