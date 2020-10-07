# coding: utf-8
"""
Factory to create Rule instances.
"""

import traceback
from easyrules.api import Facts
from easyrules.core import DefaultRule
from easyrules.utils import logger
from .abstract_rule_factory import AbstractRuleFactory
from .abstract_rule_definition_reader import AbstractRuleDefinitionReader
from .rule_definition import RuleDefinition


def eval_evaluate_method(condition: str):
    def evaluate(facts: Facts):
        try:
            result = eval(condition)
            if not isinstance(result, bool):
                logger.warning('Not a bool result when eval evaluate string')
                return False
            return result
        except Exception:
            logger.error('Error occur when eval evaluate method from yaml file, %s' % traceback.format_exc())
            return False

    return evaluate


def eval_execute_method(actions: str):
    def execute(facts: Facts):
        try:
            for action in actions:
                eval(action)
        except Exception:
            logger.error('Error occur when eval execute method from yaml file, %s' % traceback.format_exc())

    return execute


class YamlRuleFactory(AbstractRuleFactory):
    def __init__(self, reader: AbstractRuleDefinitionReader = None):
        self._reader = reader

    def create_rules(self, file_path: str):
        """
        Create a set of Rule from a yaml file.
        :return: a set of default/composite rules.
        """
        if not self._reader:
            logger.warn('No rule definition reader inited')
            return []

        rules = []
        rule_definitions = self._reader.read(file_path)
        for rule_definition in rule_definitions:
            rule = self.create_rule(rule_definition)
            rules.append(rule)
        return rules

    def create_simple_rule(self, rule_definition: RuleDefinition):
        rule = DefaultRule(
            name=rule_definition.name,
            description=rule_definition.description,
            domain=rule_definition.domain,
            priority=rule_definition.priority
        )
        # TODO, here how to 转字符串为代码？？？
        rule.evaluate = eval_evaluate_method(rule_definition.condition)
        rule.execute = eval_execute_method(rule_definition.actions)
        return rule


if __name__ == '__main__':
    obj = YamlRuleFactory().create_rules('composite-rules.yaml')
