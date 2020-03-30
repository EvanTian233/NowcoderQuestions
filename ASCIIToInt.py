"""
字符个数统计
https://www.nowcoder.com/practice/eb94f6a5b2ba49c6ac72d40b5ce95f50?tpId=37&tqId=21233&tPage=1&rp=&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking

题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。
输入描述:
输入N个字符，字符在ACSII码范围内。
输出描述:
输出范围在(0~127)字符的个数。

"""

# Before
s = list(set(input()))
count = 0
for char in s:
    if ord(char) in range (0,128):
        count +=1
print(count)

# After
while True:
    try:
        def checkStr(s):
            s = list(set(s))
            count = 0
            for char in s:
                if ord(char) in range (0,128):
                    count +=1
            return(count)
        string = input()
        print(checkStr(string))
    except:
        break