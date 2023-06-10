import os

# windows下首先应该锁定参数
if os.name == 'nt':
    from functools import partial
    import subprocess

    subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

# 获取Node版本
print(execjs.get().name)

# 方法一
js = """
'鲁班_王昭君_猴子_亚瑟_蔡文姬'.split("_")
"""
res = execjs.eval(js)
print(res)

# 方法二
with open('../00_素材箱/pyexecjs.js', 'r', 1, 'utf-8') as f:
    js_code = f.read()
    cjs = execjs.compile(js_code)
    result = cjs.call('ahh', 4, 5)
print(result)
