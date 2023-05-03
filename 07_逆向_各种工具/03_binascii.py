# 所有的东西. 到了内存层面都是：字节 -> 8个二进制 -> 数字 -> 十六进制
import base64
import binascii

b = 'Aaa我爱吃西瓜aZ!'.encode('utf-8')
print(b, type(b))  # 每个字节均是由2位16进制数组成

# 十六进制(ascii)和字节(byte)之间可以相互转化
# 字节转换为16进制数
c = binascii.b2a_hex(b)
print(c, type(c))

# 16进制数转换为字节
s = '1342536475abcde12f'
# 转化关系：两个数字 -> 一个字节
print(len(s))  # s的长度必须的偶数，因为2个16进制数转化为1个字节
print(binascii.a2b_hex(s))
