import execjs

# 获取运行js的外部环境
print(execjs.get())

print('--------------------')

# 初步运行js, eval只能运行一句话
js_code = """
(function fn(){
    return '你好';
})()
"""
r = execjs.eval(js_code)
print(r)

print('--------------------')

# 读取js文件运行js
with open('./02_js_test.js', 'r', True, 'utf-8') as f:
    js_code = execjs.compile(f.read())
    r2 = js_code.call('fn', 12)
    print(r2)
    print(type(r2))
