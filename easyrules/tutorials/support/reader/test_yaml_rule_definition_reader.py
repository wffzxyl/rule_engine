# coding: utf-8

from easyrules import YamlRuleDefinitionReader

reader = YamlRuleDefinitionReader()
rule_dicts = reader.load_rule_dicts('composite-rules.yaml')
print(rule_dicts)