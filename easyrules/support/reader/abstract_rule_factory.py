# coding: utf-8
"""
Base class for rule factories.
"""

from abc import ABCMeta, abstractmethod
from easyrules.config import CompositeRuleType
from easyrules.utils import logger
from .rule_definition import RuleDefinition
from ..composite import CompositeRule, ActivationRuleGroup, ConditionalRuleGroup, UnitRuleGroup


class AbstractRuleFactory(metaclass=ABCMeta):
    def create_rule(self, rule_definition: RuleDefinition) -> CompositeRule:
        logger.debug('Create rule with rule_definition: %s' % rule_definition)
        if rule_definition.is_composing_rule():
            return self.create_composite_rule(rule_definition)
        else:
            return self.create_simple_rule(rule_definition)

    @abstractmethod
    def create_simple_rule(self, rule_definition: RuleDefinition) -> CompositeRule:
        pass

    def create_composite_rule(self, rule_definition: RuleDefinition):
        if rule_definition.condition:
            logger.warning('Condition %s in a composite rule %s of type %s will be ignored.' %
                           (rule_definition.condition, rule_definition.name, rule_definition.get_composite_rule_type()))

        if rule_definition.actions:
            logger.warning('Actions %s in a composite rule %s of type %s will be ignored.' %
                           (rule_definition.actions, rule_definition.name, rule_definition.get_composite_rule_type()))

        composite_rule_type = rule_definition.get_composite_rule_type()
        if composite_rule_type == CompositeRuleType.ACTIVATION_RULE_GROUP.value:
            composite_rule = ActivationRuleGroup()
        elif composite_rule_type == CompositeRuleType.CONDITIONAL_RULE_GROUP.value:
            composite_rule = ConditionalRuleGroup()
        elif composite_rule_type == CompositeRuleType.UNIT_RULE_GROUP.value:
            composite_rule = UnitRuleGroup()
        else:
            raise TypeError('Invalid composite rule type in composite rule: %s, must be one of '
                            'ActivationRuleGroup, ConditionalRuleGroup, UnitRuleGroup' % rule_definition.name)

        composite_rule.name = rule_definition.name
        composite_rule.description = rule_definition.description
        composite_rule.domain = rule_definition.domain
        composite_rule.priority = rule_definition.priority

        for sub_rule_definition in rule_definition.get_composing_rules():
            composite_rule.add_rule(self.create_rule(sub_rule_definition))

        return composite_rule
