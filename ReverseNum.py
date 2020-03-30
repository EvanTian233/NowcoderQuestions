"""
数字颠倒
https://www.nowcoder.com/practice/ae809795fca34687a48b172186e3dafe?tpId=37&tqId=21234&tPage=1&rp=&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking

题目描述
描述：
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001

输入描述:
输入一个int整数
输出描述:
将这个整数以字符串的形式逆序输出

"""


# Old
while True:
    try:
        l = list(input())
        ans = ''
        for c in reversed(l):
            ans+=c
        print(ans)
    except:
        break
       
# New 
print(input()[::-1])