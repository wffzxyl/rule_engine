# coding: utf-8

import sys
from easyrules.api import Action, Condition
from .default_rule import DefaultRule

class RuleBuilder():
    def __init__(self):
        self._name = 'rule'
        self._description = 'description'
        self._priority = sys.maxsize
        self._domain = 'None'
        self._condition = False
        self._actions = []

    def name(self, name):
        # Set rule name.
        self._name = name
        return self

    def description(self, description):
        # Set rule description.
        self._description = description
        return self

    def domain(self, domain):
        # Set rule domain.
        self._domain = domain
        return self

    def priority(self, priority):
        # Set rule priority.
        self._priority = priority
        return self

    def when(self, condition: Condition):
        # Set rule condition.
        self._condition = condition
        return self

    def then(self, action: Action):
        # Add an action to the rule.
        self._actions.append(action)
        return self

    def build(self):
        # Create a new DefaultRule
        return DefaultRule(self._name, self._description, self._domain, self._priority, self._condition, self._actions)
