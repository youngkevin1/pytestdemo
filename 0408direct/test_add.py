#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：hogwarts-study 
@File    ：test_add.py
@IDE     ：PyCharm 
@Author  ：kevin
@Date    ：2021/4/11 13:09 
"""
import pytest
from decimal import *
from Calculator import Calculator

class TestCal:

    def setup_class(self):
        print("【开始计算】")
        self.calc = Calculator()

    def teardown_class(self):
        print("【计算结束】")

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [0.1, 0.1, 0.2], [1000, 1000, 2000], [0, 1000, 1000], [1.222222, 2.3333333331, 3.5555553331],
        (-1, -2, -3), (-1, 5, 4),(Decimal('-1.012345'), Decimal('2.01234567'), Decimal('1.00000067')), (0, -1.2, -1.2),
        (-1.012345, 2.01234567,1.00000067)
    ], ids=['int1', 'float', 'bignum', 'zeronum', 'bigfloat', 'negative-neg', 'negative-positive', 'decimal', 'zero-negative', 'except'])
    def test_add(self, a, b, expect):
        try:
            assert expect == self.calc.add(a, b)
        except Exception as e:
            print(f"这里有个异常：{e}")


