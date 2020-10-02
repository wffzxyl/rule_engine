# coding: utf-8

import logging
import traceback
from easyrules.api import Facts, Rule, Rules, RulesEngine, RulesEngineParameters
from .abstract_rules_engine import AbstractRulesEngine

logger = logging.getLogger("easyrules")
logger.addHandler(logging.NullHandler())


class DefaultRuleEngine(AbstractRulesEngine):
    def __init__(self, parameters: RulesEngineParameters = None):
        super(DefaultRuleEngine, self).__init__(parameters)

    # def set_connection(self, ip, port):
    #     # TODO, 保持链接，将数据上传到服务中
    #     pass

    def fire(self, rules: Rules, facts: Facts):
        self._trigger_listeners_before_fire(rules, facts)
        self._do_fire(rules, facts)
        self._trigger_listeners_after_fire(rules, facts)

    def _do_fire(self, rules: Rules, facts: Facts):
        # TODO， kbqa_engine，每次从外部代码或配置文件，实时加载所有rules，可以配置出发前后Listeners
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
            if rule.evaluate(facts):
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
                    rule.execute(facts)  # TODO, 添加返回值，或者修改facts中的recorder？
                    logger.debug("Rule %s performed successfully" % name)
                    self._trigger_listeners_on_sucess(rule, facts)
                    if self._parameters.skip_on_first_applied_rule:
                        print("Next rules will be skipped since parameter skip_on_first_applied_rule is set")
                        break
                except Exception as e:
                    logger.error("Rule %s executed with error, %s" % (name, e))
                    self._trigger_listeners_on_failure(rule, facts)
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

    def should_be_evaluated(self, rule: Rule, facts: Facts):
        # TODO，在Facts，Fact中添加domain私有变量，首先判断rule和fact是不是同一个domain中的；可以放在_trigger_listeners_before_evaluate
        return self._trigger_listeners_before_evaluate(rule, facts)

    def _trigger_listeners_before_fire(self, rules: Rules, facts: Facts):
        # rulesEngineListeners.forEach(rulesEngineListener -> rulesEngineListener.beforeEvaluate(rule, facts));
        return True

    def _trigger_listeners_after_fire(self, rules: Rules, facts: Facts):
        # rulesEngineListeners.forEach(rulesEngineListener -> rulesEngineListener.afterExecute(rule, facts));
        return True

    def _trigger_listeners_before_evaluate(self, rule: Rule, facts: Facts):
        # return ruleListeners.stream().allMatch(ruleListener -> ruleListener.beforeEvaluate(rule, facts));
        return True

    def _trigger_listeners_on_evaluate_error(self, rules: Rules, facts: Facts, exception: Exception):
        # ruleListeners.forEach(ruleListener -> ruleListener.onEvaluationError(rule, facts, exception));
        pass

    def _trigger_listeners_after_evaluate(self, rules: Rules, facts: Facts, evaluation_result: bool):
        # ruleListeners.forEach(ruleListener -> ruleListener.afterEvaluate(rule, facts, evaluationResult));
        pass

    def _trigger_listeners_before_execute(self, rules: Rules, facts: Facts):
        # ruleListeners.forEach(ruleListener -> ruleListener.beforeExecute(rule, facts));
        return True

    def _trigger_listeners_on_sucess(self, rules: Rules, facts: Facts):
        # ruleListeners.forEach(ruleListener -> ruleListener.onSuccess(rule, facts));
        return True

    def _trigger_listeners_on_failure(self, rules: Rules, facts: Facts):
        # ruleListeners.forEach(ruleListener -> ruleListener.onFailure(rule, facts, exception));
        return True
