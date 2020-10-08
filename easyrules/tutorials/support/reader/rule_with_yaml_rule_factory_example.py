# coding: utf-8

from easyrules import YamlRuleDefinitionReader, YamlRuleFactory
from easyrules import Facts, Rules, DefaultRuleEngine

# s1: Get facts.
facts = Facts()

# s2: Get rules from yaml file.
reader = YamlRuleDefinitionReader()
factory = YamlRuleFactory(reader)
rules_ = factory.create_rules('composite-rules.yaml')

# s3: Add rules to Rules instance.
rules = Rules()
rules.add(*rules_)

# s4: Define DefaultRuleEngine object and fire rules for target facts.
engine = DefaultRuleEngine()
engine.fire(rules, facts)
