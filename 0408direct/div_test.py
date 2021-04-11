#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：hogwarts-study 
@File    ：div_test.py
@IDE     ：PyCharm 
@Author  ：kevin
@Date    ：2021/4/11 13:10 
"""

import pytest
from Calculator import Calculator

class TestCal:

    def setup_class(self):
        print("【开始计算】")
        self.calc = Calculator()

    def teardown_class(self):
        print("【计算结束】")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [0.1, 0.1, 1], [1000, 1000, 1], [0, 1000, 0], [-1, -2, 0.5], (123, 0, 0)
    ], ids=['int1', 'float', 'bignum', 'zeronum', 'negative', 'exception'])
    def test_div(self, a, b, expect):
        try:
            assert expect == self.calc.div(a, b)
        except Exception as e:
            print(f"Here is a exception:{e}")