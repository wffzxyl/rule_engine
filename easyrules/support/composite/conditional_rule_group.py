# coding: utf-8
"""
A conditional rule group is a composite rule where the rule with the highest priority acts as a condition:
if the rule with the highest priority evaluates to true, then we try to evaluate the rest of the rules
and execute the ones that evaluate to true.
"""

from easyrules.api import Facts
from easyrules.config import DEFAULT_NAME, DEFAULT_DESCRIPTION, DEFAULT_DOMAIN, DEFAULT_PRIORITY
from .composite_rule import CompositeRule


class ConditionalRuleGroup(CompositeRule):
    def __init__(self,
                 name: str = DEFAULT_NAME,
                 description: str = DEFAULT_DESCRIPTION,
                 domain: str = DEFAULT_DOMAIN,
                 priority: int = DEFAULT_PRIORITY,
                 ):
        super(ConditionalRuleGroup, self).__init__(name, description, domain, priority)
        self._conditional_rule = None
        self._successful_evaluations = set()

    def evaluate(self, facts: Facts) -> bool:
        if len(self._rules) == 0:
            return False

        self._conditional_rule = self._get_rule_with_highest_priority()
        if not self._conditional_rule:
            return False

        self._successful_evaluations = set()
        for rule in self._rules:
            if rule != self._conditional_rule and rule.evaluate(facts):
                self._successful_evaluations.add(rule)
        return True

    def execute(self, facts: Facts):
        self._conditional_rule.execute(facts)
        successful_evaluations = list(set(self._successful_evaluations))
        successful_evaluations.sort(key=lambda rule: rule.priority, reverse=False)
        for rule in successful_evaluations:
            rule.execute(facts)

    def _get_rule_with_highest_priority(self):
        if len(self._rules) == 0:
            return None

        rules = list(self._rules)
        rules.sort(key=lambda rule: rule.priority, reverse=False)
        highest = rules[0]
        if len(rules) > 1 and rules[1].priority == highest.priority:
            raise ValueError('Only one rule can have highest priority')
        return highest
