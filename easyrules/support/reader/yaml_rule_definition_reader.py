# coding: utf-8
"""
Rule definition reader based on Yaml.
This reader expects a collection of rule definitions as input even for a single rule. For example:
rule1
---
rule2
"""

import yaml
from typing import List
from .abstract_rule_definition_reader import AbstractRuleDefinitionReader


class YamlRuleDefinitionReader(AbstractRuleDefinitionReader):
    def load_rule_dicts(self, file_path: str) -> List:
        """
        Read a list of rule definitions from a rule config file.
        The rule config file is expected to contain a collection of rule definitions even for a single rule.
        :return: a list of rule definitions
        """
        rule_dicts = []
        with open(file_path, 'r') as fp:
            rule_yaml_objects = yaml.load_all(fp, Loader=yaml.FullLoader)
            for rule_dict in rule_yaml_objects:
                rule_dicts.append(rule_dict)
        return rule_dicts
