# coding: utf-8
"""
Builder to create Rule instances.
"""

from easyrules.api import Action, Condition
from easyrules.config import DEFAULT_NAME, DEFAULT_DESCRIPTION, DEFAULT_DOMAIN, DEFAULT_PRIORITY
from .default_rule import DefaultRule


class RuleBuilder():
    def __init__(self):
        self._name = DEFAULT_NAME,
        self._description = DEFAULT_DESCRIPTION,
        self._domain = DEFAULT_DOMAIN,
        self._priority = DEFAULT_PRIORITY,
        self._condition = None
        self._actions = []

    def name(self, name: str):
        # Set rule name.
        self._name = name
        return self

    def description(self, description: str):
        # Set rule description.
        self._description = description
        return self

    def domain(self, domain: str):
        # Set rule domain.
        self._domain = domain
        return self

    def priority(self, priority: int):
        # Set rule priority.
        self._priority = priority
        return self

    def when(self, condition: Condition):
        # Set rule Condition object.
        self._condition = condition
        return self

    def then(self, action: Action):
        # Add an Action object to the rule.
        self._actions.append(action)
        return self

    def build(self):
        # Create a new DefaultRule
        return DefaultRule(self._name, self._description, self._domain, self._priority, self._condition, self._actions)
