# coding: utf-8

import copy
import logging
from easyrules.api import Facts, Rules, RulesEngine, RulesEngineParameters

logger = logging.getLogger("easyrules")
logger.addHandler(logging.NullHandler())


class AbstractRulesEngine(RulesEngine):
    def __init__(self, parameters: RulesEngineParameters = None):
        self._parameters = parameters if parameters else RulesEngineParameters()
        self._rule_listeners = []
        self._rule_engine_listeners = []

    def get_parameters(self):
        # Return a copy of the rules engine parameters.
        return copy.deepcopy(self._parameters)

    def register_rule_listener(self):
        # TODO, ADD paramter rulesListeners and other code
        pass

    def get_rule_listeners(self):
        # Return the list of registered rule listeners.
        return self._rule_listeners

    def register_rule_engine_listener(self):
        # TODO, ADD paramter rulesEngineListeners and other code
        pass

    def get_rule_engine_listeners(self):
        # Return the list of registered rules engine listeners.
        return self._rule_engine_listeners

    def fire(self, rules: Rules, fact: Facts):
        # Fire all registered rules on given facts.
        pass

    def check(self, rules: Rules, fact: Facts):
        """
        Check rules without firing
        :return: a dict with the result of evaluation of each rule
        """
        return {}
