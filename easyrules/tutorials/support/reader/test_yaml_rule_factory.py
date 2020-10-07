# coding: utf-8

from easyrules import YamlRuleDefinitionReader, YamlRuleFactory

reader = YamlRuleDefinitionReader()
factory = YamlRuleFactory(reader)
rules = factory.create_rules('composite-rules.yaml')
print(rules)