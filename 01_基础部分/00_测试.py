import json

a = {
    "name": "张三",
    "age": 18,
    'hobbies': ["吃饭", "睡觉", "打豆豆"]
}
print(json.dumps(a, separators=(',', ':'), ensure_ascii=False))

