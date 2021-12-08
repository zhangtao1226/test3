# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 07:30
# @Author  : zhangtao
# @File    : 初级算法.py
# @Software: PyCharm

# 1、删除排序数组中的重复项

def removeDuplicates(nums):
    """
    快慢指针循环比较
    :param nums:
    :return:
    """
    length = len(nums)
    i, j = 0, 1
    for x in range(i, length - 1):
        for y in range(j, length):
            if nums[x] == nums[y]:
                del nums[x]

            i += 1
            j += 1

    print(nums)

nums = [1, 2, 3, 3, 2]
removeDuplicates(nums)