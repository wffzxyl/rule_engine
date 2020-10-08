# coding: utf-8

from easyrules import RuleDecorator, Fact, Rule, Facts, Rules, DefaultRuleEngine
from typing import List

# s1: Get facts.
facts = Facts()


# s2: define a Rule subclass with RuleDecorator
@RuleDecorator(name='hello_word', description='desc', domain='example', priority=2)
class HelloWorldRule(Rule):
    def evaluate(self, facts: List[Fact]):
        return True

    def execute(self, facts: List[Fact]):
        print('hello_word')


@RuleDecorator(name='do_sth', domain='example', priority=1)
class DoSthRule(Rule):
    def evaluate(self, facts: List[Fact]):
        return True

    def execute(self, facts: List[Fact]):
        print('do sth')


# s3: Define some rules instances.
rule1 = HelloWorldRule()
rule2 = DoSthRule()

# s4: Add rules to Rules instance.
rules = Rules()
rules.add(rule1)
rules.add(rule2)

# s5: Define DefaultRuleEngine object and fire rules for target facts.
engine = DefaultRuleEngine()
engine.fire(rules, facts)
