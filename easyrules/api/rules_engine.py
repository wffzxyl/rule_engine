# coding: utf-8
"""
Rules engine interface.
"""

from abc import ABCMeta, abstractmethod
from typing import Dict, List
from .facts import Facts
from .rules import Rules
from .rule_engine_listener import RulesEngineListener
from .rule_listener import RuleListener


class RulesEngine(metaclass=ABCMeta):
    def get_parameters(self):
        # Get the parameters.
        return None

    def get_rule_listeners(self) -> List[RuleListener]:
        # Return the list of registered rule listeners.
        return []

    def get_rule_engine_listeners(self) -> List[RulesEngineListener]:
        # Return the list of registered rules engine listeners.
        return []

    @abstractmethod
    def fire(self, rules: Rules, fact: Facts):
        # Fire all registered rules on given facts.
        pass

    def check(self, rules: Rules, fact: Facts) -> Dict:
        """
        Check rules without firing
        :return: a dict with the result of evaluation of each rule
        """
        return {}
