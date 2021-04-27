# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 19:52
# @Author  : zhangtao
# @File    : 练习一.py
# @Software: PyCharm

class Solution:

    def isValid(self, s):
        if not s or len(s) == 0:
            return True
        if len(s) % 2 == 1:
            return False

        t = []
        for c in s:
            if c == "(":
                t.append(c)
            elif c == ")":
                if len(t) == 0:
                    return False
                t.pop()
            else:
                return False
        return len(t) == 0

solution = Solution()

assert not solution.isValid("(")
