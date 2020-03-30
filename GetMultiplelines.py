"""
字串的连接最长路径查找
https://www.nowcoder.com/practice/5af18ba2eb45443aa91a11e848aa6723?tpId=37&tqId=21237&tPage=1&rp=&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking

输入描述:
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述:
数据输出n行，输出结果为按照字典序排列的字符串。
示例1
输入

复制
9
cap
to
cat
card
two
too
up
boat
boot
输出

复制
boat
boot
cap
card
cat
to
too
two
up
"""


n=int(input())
s=[]
for i in range(n):
    s.append(input())
result=sorted(s)
for i in result:
    print(i)