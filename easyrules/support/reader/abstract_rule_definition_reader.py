# coding: utf-8
"""
Base class for RuleDefinitionReader.
"""

from typing import Dict, List
from abc import abstractmethod
from easyrules.config import DEFAULT_NAME, DEFAULT_DESCRIPTION, DEFAULT_DOMAIN, DEFAULT_PRIORITY
from easyrules.utils import logger
from .rule_definition import RuleDefinition
from .rule_definition_reader import RuleDefinitionReader


class AbstractRuleDefinitionReader(RuleDefinitionReader):
    def read(self, file_path: str):
        logger.debug('Load rule dicts from %s' % file_path)
        rule_definitions = []
        rule_dicts = self.load_rule_dicts(file_path)
        for rule_dict in rule_dicts:
            rule_definition = self.create_rule_definition(rule_dict)
            rule_definitions.append(rule_definition)
        return rule_definitions

    @abstractmethod
    def load_rule_dicts(self, file_path: str) -> List:
        pass

    def create_rule_definition(self, rule_dict: Dict):
        rule_definition = RuleDefinition()
        rule_definition.name = rule_dict.get('name', DEFAULT_NAME)
        rule_definition.description = rule_dict.get('description', DEFAULT_DESCRIPTION)
        rule_definition.domain = rule_dict.get('domain', DEFAULT_DOMAIN)
        rule_definition.priority = rule_dict.get('priority', DEFAULT_PRIORITY)
        rule_definition.condition = rule_dict.get('condition', None)
        rule_definition.actions = rule_dict.get('actions', [])

        composite_rule_type = rule_dict.get("compositeRuleType", None)
        if not composite_rule_type and not rule_definition.condition:
            raise ValueError('The rule condition must be specified')
        if not composite_rule_type and not rule_definition.actions:
            raise ValueError('The rule action(s) must be specified')

        composing_rules = rule_dict.get('composingRules', [])
        if not composite_rule_type and len(composing_rules) != 0:
            raise ValueError('Non-composite rules cannot have composing rules')
        elif composite_rule_type and len(composing_rules) == 0:
            raise ValueError('Composite rules must have composing rules specified')
        elif composing_rules:
            composite_rule_definitions = []
            for sub_rule_dict in composing_rules:  # rule_dict format is same as k_2_v
                sub_rule_definition = self.create_rule_definition(sub_rule_dict)
                composite_rule_definitions.append(sub_rule_definition)

            rule_definition.set_composite_rule_type(composite_rule_type)
            rule_definition.set_composing_rules(composite_rule_definitions)
        return rule_definition
