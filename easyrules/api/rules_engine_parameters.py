# coding: utf-8
"""
Parameters of a rules engine.
When parameters are used with a DefaultRulesEngine object, they are applied on all registered rules.
When parameters are used with a InferenceRulesEngine object, they are applied on candidate rules in each iteration.
"""

import sys


class RulesEngineParameters(object):
    def __init__(self,
                 skip_on_first_applied_rule=False,
                 skip_on_first_failed_rule=False,
                 skip_on_first_non_triggered_rule=False,
                 rule_priority_threshold=sys.maxsize):
        """
        :param skip_on_first_applied_rule: parameter to skip next applicable rules on first applied rule
        :param skip_on_first_failed_rule: parameter to skip next applicable rules on first failed rule
        :param skip_on_first_non_triggered_rule: parameter to skip next applicable rules on first non triggered rule
        :param rule_priority_threshold: threshold after which rules should be skipped
        """
        self._skip_on_first_applied_rule = skip_on_first_applied_rule
        self._skip_on_first_failed_rule = skip_on_first_failed_rule
        self._skip_on_first_non_triggered_rule = skip_on_first_non_triggered_rule
        self._rule_priority_threshold = rule_priority_threshold

    @property
    def skip_on_first_applied_rule(self):
        return self._skip_on_first_applied_rule

    @property
    def skip_on_first_failed_rule(self):
        return self._skip_on_first_failed_rule

    @property
    def skip_on_first_non_triggered_rule(self):
        return self._skip_on_first_non_triggered_rule

    @property
    def rule_priority_threshold(self):
        return self._rule_priority_threshold

    def __repr__(self):
        return "RulesEngineParameters{{" \
               "skip_on_first_applied_rule=%s, " \
               "skip_on_first_failed_rule=%s, " \
               "skip_on_first_non_triggered_rule=%s, " \
               "rule_priority_threshold=%s.}}" % (
            self._skip_on_first_applied_rule,
            self._skip_on_first_failed_rule,
            self._skip_on_first_non_triggered_rule,
            self._rule_priority_threshold)

    __str__ = __repr__
