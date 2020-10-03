# coding: utf-8
"""
A unit rule group is a composite rule that acts as a unit: Either all rules are applied
or nothing is applied ((AND logic, all or nothing semantic).
"""

from easyrules.api import Facts
from easyrules.config import DEFAULT_NAME, DEFAULT_DESCRIPTION, DEFAULT_DOMAIN, DEFAULT_PRIORITY
from .composite_rule import CompositeRule


class UnitRuleGroup(CompositeRule):
    def __init__(self,
                 name: str = DEFAULT_NAME,
                 description: str = DEFAULT_DESCRIPTION,
                 domain: str = DEFAULT_DOMAIN,
                 priority: int = DEFAULT_PRIORITY,
                 ):
        super(UnitRuleGroup, self).__init__(name, description, domain, priority)
        self._selected_rule = None

    def evaluate(self, facts: Facts):
        if len(self._rules) == 0:
            return False

        for rule in self._rules:
            if not rule.evaluate(facts):
                return False
        return True

    def execute(self, facts: Facts):
        if len(self._rules) == 0:
            return False

        rules = list(self._rules)
        rules.sort(key=lambda rule: rule.priority, reverse=False)
        for rule in rules:
            rule.execute(facts)
