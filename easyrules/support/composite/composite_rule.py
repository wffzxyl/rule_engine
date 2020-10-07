# coding: utf-8
"""
 Base class representing a composite rule composed of a set of rules.
"""

from abc import abstractmethod
from typing import Set
from easyrules.api import Facts, Rule
from easyrules.config import DEFAULT_NAME, DEFAULT_DESCRIPTION, DEFAULT_DOMAIN, DEFAULT_PRIORITY


class CompositeRule(Rule):
    def __init__(self,
                 name: str = DEFAULT_NAME,
                 description: str = DEFAULT_DESCRIPTION,
                 domain: str = DEFAULT_DOMAIN,
                 priority: int = DEFAULT_PRIORITY,
                 ):
        super(CompositeRule, self).__init__(name, description, domain, priority)
        self._rules: Set[Rule] = set()

    @abstractmethod
    def evaluate(self, facts: Facts) -> bool:
        return True

    @abstractmethod
    def execute(self, facts: Facts):
        pass

    def add_rule(self, rule: Rule):
        # Add a rule to the composite rule.
        if not rule: raise TypeError('rule must not be None')
        self._rules.add(rule)

    def remove_rule(self, rule: Rule):
        # Remove one rule.
        if not rule: raise TypeError('rule must not be None')
        rule = self.get_by_name(rule.name)
        if rule:
            self._rules.remove(rule)

    def get_by_name(self, rule_name: str):
        # Get a rule by its name, or return None.
        if not rule_name: raise TypeError('rule name must not be None')
        for rule in self._rules:
            if rule.name == rule_name:
                return rule
        return None

    def __repr__(self):
        return 'Rule{name=%s, description=%s, domain=%s, priority=%s, _rules=%s}' % (
            self._name, self._description, self._domain, self._priority, self._rules)

    __str__ = __repr__
