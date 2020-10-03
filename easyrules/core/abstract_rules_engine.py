# coding: utf-8
"""
Base class for RulesEngine implementations.
"""

import copy
from typing import List
from easyrules.api import RulesEngine, RulesEngineParameters
from easyrules.api import RuleListener, RulesEngineListener


class AbstractRulesEngine(RulesEngine):
    def __init__(self, parameters: RulesEngineParameters = None):
        self._parameters: RulesEngineParameters = parameters if parameters else RulesEngineParameters()
        self._rule_listeners: List[RuleListener] = []
        self._rule_engine_listeners: List[RulesEngineListener] = []

    def get_parameters(self):
        # Return a copy of the rules engine parameters.
        return copy.deepcopy(self._parameters)

    def get_rule_listeners(self):
        # Return the list of registered rule listeners.
        return self._rule_listeners

    def get_rule_engine_listeners(self):
        # Return the list of registered rules engine listeners.
        return self._rule_engine_listeners

    def register_rule_listener(self, rule_listener: RuleListener):
        self._rule_listeners.append(rule_listener)

    def register_rule_listeners(self, rule_listeners: List[RuleListener]):
        self._rule_listeners.extend(rule_listeners)

    def register_rule_engine_listener(self, rule_engine_listener: RulesEngineListener):
        self._rule_engine_listeners.append(rule_engine_listener)

    def register_rule_engine_listeners(self, rule_engine_listeners: List[RulesEngineListener]):
        self._rule_engine_listeners.extend(rule_engine_listeners)
