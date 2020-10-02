# coding: utf-8

import sys
from typing import List
from easyrules.api import Action, Condition, Facts, Rule


class DefaultRule(Rule):
    def __init__(self,
                 name: str = 'rule',
                 description: str = 'description',
                 domain: str = None,
                 priority: int = sys.maxsize,
                 condition: Condition = None,
                 actions: List[Action] = None,
                 ):
        super(DefaultRule, self).__init__(name, description, domain, priority)
        self._condition = condition
        self._actions = actions if actions else []

    def evaluate(self, facts: Facts):
        # TODO, change to multi conditions by &&.
        return self._condition.evaluate(facts)

    def execute(self, facts: Facts):
        # TODO, return result list
        for action in self._actions:
            action.execute(facts)

    def check_domain(self, domain):
        # TODO, check it in listeners or engine listeners.
        pass
