import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

# RSA：加密和解密用的不是同一把钥匙
# RSA适用于客户端向服务器发送加密数据，数据在客户端使用公钥进行加密，服务器端使用私钥进行解密

# 使用RSA管理公钥和私钥
# 公钥和私钥生成一次就行了，不用一直生成
rsa_key = RSA.generate(1024)
private_key = rsa_key.export_key('PEM')
print(type(private_key))  # 生成的Key是字节,是私钥
with open('../00_素材箱/private_key.pem', "wb") as f:
    f.write(private_key)
# base64转换成字符串
pri_key_str = base64.b64encode(private_key).decode()
print(pri_key_str)

print('--------------------')

# 用私钥可以生成公钥, 调用public_key() 拿到公钥
public_key = rsa_key.public_key().export_key('PEM')
with open('../00_素材箱/public_key.pem', "wb") as f:
    f.write(public_key)
# base64转换成字符串
pub_key_str = base64.b64encode(public_key).decode()
print(pub_key_str)

print('--------------------')

# 进行RSA加密
s = '哈哈哈哈嘻嘻嘻1234%……&^……'
# 处理成字节
ming_bs = s.encode('utf-8')
# 加载公钥
with open('../00_素材箱/public_key.pem', 'rb') as f:  # 因为key本身就是字节，所以用rb模式打开文件
    public_key = RSA.import_key(f.read())
# 创建加密器
rsa = PKCS1_v1_5.new(public_key)
# 加密
mi_bs = rsa.encrypt(ming_bs)
# 加密结果处理成base64
mi_str = base64.b64encode(mi_bs).decode()
print(mi_str)

print('--------------------')

# 进行RSA解密 (不重要，因为服务器永远不会给你私钥)
# 加载私钥
with open('../00_素材箱/private_key.pem', 'rb') as f:
    private_key = RSA.import_key(f.read())
# 创建加密器
rsa = PKCS1_v1_5.new(private_key)
# 解密
mi_bs = base64.b64decode(mi_str)
ming_bs = rsa.decrypt(mi_bs, None)  # ciphertext设为None
ming = ming_bs.decode('utf-8')
print(ming)
