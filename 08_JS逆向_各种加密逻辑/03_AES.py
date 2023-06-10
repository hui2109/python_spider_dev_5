import base64
import binascii

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# 安装包：pip install pycryptodome
# 对称加密：加密和解密时使用的秘钥是同一个.
# AES, DES, 3DES

# 小总结:
# 加密:
# 明文字符串 -> 处理成字节 -> 进行填充(pad)  ->  加密  ->  密文(字节)  ->  (base64处理|十六进制字符串) -> 加密字符串
# 解密：
# 明文字符串 <- 明文字节  <- 解开填充(unpad) <-  解密  <-  密文(字节)  <-  (base64处理|十六进制字符串) <- 加密字符串

# key: 通常是16位的字节，还可以是24、32位的字节
# mode: CBC(需要iv), ECB(不需要iv)
# iv: CBC模式下必须是16位的字节

# 加密
aes = AES.new(key='aaaaaaaaaabbbbbb'.encode('utf-8'), iv='ccccccccccffffff'.encode('utf-8'), mode=AES.MODE_CBC)

ming = '我要吃饭哈哈哈'
ming_bytes = ming.encode('utf-8')
# print(ming_bytes, len(ming_bytes))

ming_bytes_pad = pad(ming_bytes, 16)
# print(ming_bytes_pad, len(ming_bytes_pad))

mi_bytes = aes.encrypt(ming_bytes_pad)
print(mi_bytes, len(ming_bytes))

# 使用base64或者binascii处理成字符串
mi_base64 = base64.b64encode(mi_bytes).decode()
# print(mi_base64, len(mi_base64))

mi_binascii = binascii.b2a_hex(mi_bytes)
print(mi_binascii, len(mi_binascii))

print('--------------------')

# 解密
# 必须重新造一个解密器，不能使用之前的加密器
aes = AES.new(key='aaaaaaaaaabbbbbb'.encode('utf-8'), iv='ccccccccccffffff'.encode('utf-8'), mode=AES.MODE_CBC)

# base64解密
# 这里返回的是AES加密后base64处理前的字节
mi_bytes = base64.b64decode(mi_base64)
ming_bytes_pad = aes.decrypt(mi_bytes)
ming_bytes = unpad(ming_bytes_pad, 16)
ming = ming_bytes.decode('utf-8')
print(ming)

# binascii解密
# 必须重新造一个解密器，不能使用之前的解密器
aes = AES.new(key='aaaaaaaaaabbbbbb'.encode('utf-8'), iv='ccccccccccffffff'.encode('utf-8'), mode=AES.MODE_CBC)
mi_bytes = binascii.a2b_hex(mi_binascii)
ming_bytes_pad = aes.decrypt(mi_bytes)
ming_bytes = unpad(ming_bytes_pad, 16)
ming = ming_bytes.decode('utf-8')
print(ming)
