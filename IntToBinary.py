
"""
求int型正整数在内存中存储时1的个数
https://www.nowcoder.com/practice/440f16e490a0404786865e99c6ad91c9?tpId=37&tqId=21238&tPage=1&rp=&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking

题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
输入描述:
 输入一个整数（int类型）
输出描述:
 这个数转换成2进制后，输出1的个数
"""


number = int(input())
count = 0
while number > 1:
    count += number%2
    number = number//2
print(count+1)