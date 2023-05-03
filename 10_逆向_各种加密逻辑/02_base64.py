import base64

# 数组 = [A-Z a-z 0-9 + / =]
# 将字节转换为字符串
a = 'aa我爱你Z'.encode('utf-8')
print(a)

# 将字节转换为base64自己特定的字节
b = base64.b64encode(a)
print(b)

# 将base64自己特定的字节转换为加密字符串
c = b.decode()
print(c, type(c))

# 将字符串还原为字节
d = base64.b64decode(c)
print(d)

# 特殊情況：有的网站会把base64进行特殊的处理。把+替换成-，把/替换成_
# 应对方案一：replace("+", "-").replace("/", "_")
# 应对方案二：用base64自动处理  bs = base64.b64decode(s, b"-_")
# 如果上述转化后. 进行解密操作后. 发现数据不对. 或者根本无法解密, 调换一下顺序即可

# 因为base64可以将字节转换为字符串，因此，有的网站将自己的一些【小图片】转换为字符串
# https://www.baidu.com/
img_str = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAMAAACuX0YVAAAABlBMVEVnpv85i/9PO5r4AAAAD0lEQVR42gEEAPv/AAAAAQAFAAIros7PAAAAAElFTkSuQmCC'
img_str = img_str.split(',')[1]
img_byte = base64.b64decode(img_str)
print(img_byte)

with open('../00_素材箱/base64_字符串转字节.png', 'wb') as f:
    f.write(img_byte)
