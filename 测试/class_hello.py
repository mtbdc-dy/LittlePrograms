# -*- coding: utf-8 -*-
# @Time : 2019/4/8,008 7:08
# @Author : 徐缘
# @FileName: class_hello.py
# @Software: PyCharm


class Hello:
    _a = 1

    def say_hello(self, name):
        print(self._a)
        print('hello', name)


a = Hello()
a.say_hello('Shay')


