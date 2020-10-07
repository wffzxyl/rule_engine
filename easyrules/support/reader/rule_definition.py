# coding: utf-8
"""
Base class representing a composite rule composed of a set of rules.
"""

from typing import List
from easyrules.api import Condition, Action
from easyrules.config import DEFAULT_NAME, DEFAULT_DESCRIPTION, DEFAULT_DOMAIN, DEFAULT_PRIORITY


class RuleDefinition(object):
    def __init__(self):
        self._name: str = DEFAULT_NAME
        self._description: str = DEFAULT_DESCRIPTION
        self._domain: str = DEFAULT_DOMAIN
        self._priority: int = DEFAULT_PRIORITY
        self._condition: str = None
        self._actions: str = None
        self._composite_rule_type = None
        self._composing_rules: List[RuleDefinition] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def domain(self) -> str:
        return self._domain

    @domain.setter
    def domain(self, domain: str):
        self._domain = domain

    @property
    def priority(self) -> int:
        return self._priority

    @priority.setter
    def priority(self, priority: str):
        self._priority = priority

    @property
    def condition(self) -> str:
        return self._condition

    @condition.setter
    def condition(self, condition: str):
        self._condition = condition

    @property
    def actions(self) -> str:
        return self._actions

    @actions.setter
    def actions(self, actions: str):
        self._actions = actions

    def set_composite_rule_type(self, composite_rule_type):
        self._composite_rule_type = composite_rule_type

    def set_composing_rules(self, composing_rule_definitions):  # List[RuleDefinition]
        self._composing_rules = composing_rule_definitions

    def get_composite_rule_type(self):
        return self._composite_rule_type

    def get_composing_rules(self, ):
        return self._composing_rules

    def is_composing_rule(self):
        return len(self._composing_rules) != 0

    def __repr__(self):
        repr ='RuleDefinition{' \
              'rule_type=%s, name=%s, description=%s, domain=%s, priority=%s, condition=%s, actions=%s, composing_rules=%s' \
              '}' % \
              (self._composite_rule_type, self._name, self._description, self._domain, self._priority, self._condition,
               self._actions, self._composing_rules)
        return repr

    __str__ = __repr__
