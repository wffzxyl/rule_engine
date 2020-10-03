# coding: utf-8
"""
The default rule for RuleBuilder with one Condition object and one or more Action object.
"""

from typing import List
from easyrules.api import Action, Rule, Condition, Facts
from easyrules.config import DEFAULT_NAME, DEFAULT_DESCRIPTION, DEFAULT_DOMAIN, DEFAULT_PRIORITY


class DefaultRule(Rule):
    """
    :type name: str
    :type description: str
    :type domain: str
    :type priority: int
    """
    def __init__(self,
                 name: str = DEFAULT_NAME,
                 description: str = DEFAULT_DESCRIPTION,
                 domain: str = DEFAULT_DOMAIN,
                 priority: int = DEFAULT_PRIORITY,
                 condition: Condition = None,
                 actions: List[Action] = None,
                 ):
        super(DefaultRule, self).__init__(name, description, domain, priority)
        self._condition = condition
        self._actions = actions if actions else []

    def evaluate(self, facts: Facts):
        if not self._condition:
            return False
        return self._condition.evaluate(facts)

    def execute(self, facts: Facts):
        if not self._actions:
            return
        for action in self._actions:
            action.execute(facts)
