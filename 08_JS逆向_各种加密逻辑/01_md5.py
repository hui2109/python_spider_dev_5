from hashlib import md5, sha1, sha256, sha512

# 当你在网站上看到了一些加密逻辑. 发现. 计算的结果是32位字符串
# 该字符串的组成是 0-9a-f(十六进制) 可以猜测是md5
# 然后去尝试: 把123456传递进去. 看看结果.
# 如果结果是e10开头.  直接标准md5.
# 你就可以开始写python代码了

# 注意,如果计算的结果不是e10. 这会儿. 你要小心了. 有可能是魔改的md5
# 只能抠代码....扣起来非常痛苦.

obj = md5()
obj.update('123456'.encode('utf-8'))
md5_value = obj.hexdigest()
print('md5_value', md5_value, '长度为', len(md5_value))

print('--------------------')

# 加盐
obj = md5('adfsdfgfsdgdgdfsdgfdgf'.encode('utf-8'))
obj.update('123456'.encode('utf-8'))
md5_value_with_salt = obj.hexdigest()
print('md5_value_with_salt', md5_value_with_salt, '长度为', len(md5_value_with_salt))

print('--------------------')

obj = sha1()
obj.update('123456'.encode('utf-8'))
sha1_value = obj.hexdigest()
print('sha1_value', sha1_value, '长度为', len(sha1_value))

print('--------------------')

obj = sha256()
obj.update('123456'.encode('utf-8'))
sha256_value = obj.hexdigest()
print('sha256_value', sha256_value, '长度为', len(sha256_value))

print('--------------------')

obj = sha512()
obj.update('123456'.encode('utf-8'))
sha512_value = obj.hexdigest()
print('sha512_value', sha512_value, '长度为', len(sha512_value))

print('--------------------')

# 对文件进行md5计算
obj = md5()
with open('../00_素材箱/四大名著/python-3.10.9-embed-amd64.zip', 'rb') as f:
    for i in f:
        obj.update(i)
print(obj.hexdigest() == 'c02aded21c751551d5e5ec83c3736fa7')
