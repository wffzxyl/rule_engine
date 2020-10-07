# coding: utf-8
"""
An activation rule group is a composite rule that fires the first applicable rule
and ignores other rules in the group (XOR logic).
Rules are first sorted by their natural order (priority by default) within the group.
"""

from easyrules.api import Facts
from easyrules.config import DEFAULT_NAME, DEFAULT_DESCRIPTION, DEFAULT_DOMAIN, DEFAULT_PRIORITY
from .composite_rule import CompositeRule


class ActivationRuleGroup(CompositeRule):
    def __init__(self,
                 name: str = DEFAULT_NAME,
                 description: str = DEFAULT_DESCRIPTION,
                 domain: str = DEFAULT_DOMAIN,
                 priority: int = DEFAULT_PRIORITY,
                 ):
        super(ActivationRuleGroup, self).__init__(name, description, domain, priority)
        self._selected_rule = None

    def evaluate(self, facts: Facts) -> bool:
        if len(self._rules) == 0:
            return False

        for rule in self._rules:
            if rule.evaluate(facts):
                self._selected_rule = rule
                return True
        return False

    def execute(self, facts: Facts):
        if self._selected_rule:
            self._selected_rule.execute(facts)
