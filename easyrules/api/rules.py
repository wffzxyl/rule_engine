# coding: utf-8
"""
This class encapsulates a set of rules and represents a rules namespace.
Rules must have a unique name within a rules namespace.
"""

from easyrules.utils import logger


class Rules:
    def __init__(self, rules: set = None):
        self._rules = rules if rules else set()

    def add(self, *rules):
        """
        Add one or more rules, replacing any rule with the same name.  # TODO, here replaced???
        :param fact: rule to add, must not be None
        """
        if not rules: raise TypeError('rule must not be None')
        for rule in rules:
            for rule_ in self._rules:
                if rule.name == rule_.name:
                    logger.warning('removed same name rule: %s' % rule_)
                    self._rules.remove(rule_)
            self._rules.add(rule)

    def remove(self, *rules):
        # Remove one or more rules.
        for rule in rules:
            rule = self.get_by_name(rule.name)
            if rule:
                self._rules.remove(rule)

    def get(self, rule_name: str):
        # Get a rule by its name, or return None.
        return self.get_by_name(rule_name)

    def get_by_name(self, rule_name: str):
        # Get a rule by its name, or return None.
        if not rule_name: raise TypeError('rule name must not be None')
        for rule in self._rules:
            if rule.name == rule_name:
                return rule
        return None

    def remove_by_name(self, rule_name: str):
        # Remove a rule by name.
        rule = self.get_by_name(rule_name)
        if rule:
            self._rules.remove(rule)

    def size(self):
        # Return how many rules are currently added.
        return len(self._rules)

    def empty(self):
        # Check if the rule set is empty.
        return len(self._rules) == 0

    def clear(self):
        # Clear rules.
        return self._rules.clear()

    def __repr__(self):
        return '[' + ','.join(self._rules) + ']'

    __str__ = __repr__

    def __len__(self):
        # Return the length of the set of rules.
        return len(self._rules)

    def __iter__(self):
        # Return an iterator on the list of rules ordered by priority.
        rules = list(self._rules)
        rules.sort(key=lambda rule: rule.priority, reverse=False)
        return iter(rules)
