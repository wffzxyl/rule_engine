# coding: utf-8

from easyrules import DRule, Fact, Rule, Facts, Rules, DefaultRuleEngine
from typing import List


@DRule(name='hello_word', description='desc', domain='example', priority=2)
class HelloWorldRule(Rule):
    def evaluate(self, facts: List[Fact]):
        return True

    def execute(self, facts: List[Fact]):
        print('hello_word')


@DRule(name='do_sth', description='desc', domain='example', priority=1)
class DoSthRule(Rule):
    def evaluate(self, facts: List[Fact]):
        return True

    def execute(self, facts: List[Fact]):
        print('do sth')


facts = Facts()

rule = HelloWorldRule()

rules = Rules()
rules.add(rule)
rules.add(DoSthRule())

engine = DefaultRuleEngine()
engine.fire(rules, facts)
