
"""
进制转换

题目描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）
输入描述:
输入一个十六进制的数值字符串。
输出描述:
输出该数值的十进制字符串。
"""



while True:
    try:
        print(int(input(),16))
    except:
        break