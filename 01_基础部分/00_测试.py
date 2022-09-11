import re

res = re.search('<b>.+?</b>', '<b>b标签</b><b>b标签</b>')
res1 = re.search('<b>.*?</b>', '<b>b标签</b><b>b标签</b><b>b标签</b><b>b标签</b>')

print(res.group())
print(res1.group())
