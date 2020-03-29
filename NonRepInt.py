"""
提取不重复的整数

题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
输入描述:
输入一个int型整数
输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
"""

result=""
for i in input()[::-1]:
    if i not in result:
        result+=i
print(result)