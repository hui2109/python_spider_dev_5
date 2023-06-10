# 和AES模式差不多，有如下区别
# key: 必须是8位的字节
# mode: CBC(需要iv), ECB(不需要iv)
# iv: CBC模式下必须是8位的字节

# 小总结:
# 加密:
# 明文字符串 -> 处理成字节 -> 进行填充(pad)  ->  加密  ->  密文(字节)  ->  (base64处理|十六进制字符串) -> 加密字符串
# 解密：
# 明文字符串 <- 明文字节  <- 解开填充(unpad) <-  解密  <-  密文(字节)  <-  (base64处理|十六进制字符串) <- 加密字符串

import base64

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# 加密
des = DES.new(key='gggghhhh'.encode('utf=8'), iv='uuuuoooo'.encode('gbk'), mode=DES.MODE_CBC)
ming = 'dasasdasd今天再下雨+-*/*#@%￥#……￥&%*（&）'
ming_bytes = ming.encode('gbk')
ming_bytes_pad = pad(ming_bytes, 8)
mi_bytes = des.encrypt(ming_bytes_pad)
mi = base64.b64encode(mi_bytes).decode()
print(mi)

print('--------------------')

# 解密
des = DES.new(key='gggghhhh'.encode('utf=8'), iv='uuuuoooo'.encode('gbk'), mode=DES.MODE_CBC)
mi_bytes = base64.b64decode(mi)
mi_bytes_pad = des.decrypt(mi_bytes)
ming_bytes = unpad(mi_bytes_pad, 8)
ming = ming_bytes.decode('gbk')
print(ming)
