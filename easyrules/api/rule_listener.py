# coding: utf-8
"""
A listener for rule execution events.
"""

from abc import ABCMeta, abstractmethod
from .facts import Facts
from .rule import Rule


class RuleListener(metaclass=ABCMeta):

    @abstractmethod
    def before_evaluate(self, rule: Rule, fact: Facts):
        """
        Triggered before the evaluation of a rule.
        :param rules: being evaluated
        :param fact: known before evaluating the rule
        :return: True if the rule should be evaluated, False otherwise
        """
        return True

    @abstractmethod
    def after_evaluate(self, rule: Rule, fact: Facts, after_evaluate: bool):
        """
        Triggered after the evaluation of a rule.
        :param rules: that has been evaluated
        :param fact: known after evaluating the rule
        """
        pass

    @abstractmethod
    def on_evaluation_error(self, rule: Rule, fact: Facts, exception: Exception):
        """
        Triggered on condition evaluation error due to any runtime exception.
        :param rules: that has been evaluated
        :param fact: known after evaluating the rule
        :exception: that happened while attempting to evaluate the condition
        """
        pass

    @abstractmethod
    def before_execute(self, rule: Rule, fact: Facts):
        """
        Triggered before the execution of a rule.
        :param rules: the current rule
        :param fact: known facts before executing the rule
        """
        pass

    @abstractmethod
    def on_success(self, rule: Rule, fact: Facts):
        """
        Triggered after a rule has been executed successfully.
        :param rules: the current rule
        :param fact: known facts after executing the rule
        """
        pass

    @abstractmethod
    def on_failure(self, rule: Rule, fact: Facts, exception: Exception):
        """
        Triggered after a rule has failed.
        :param rules: the current rule
        :param fact: known facts after executing the rule
        :exception: the exception thrown when attempting to execute the rule
        """
        pass
