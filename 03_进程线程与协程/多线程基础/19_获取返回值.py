import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


# import threadpool
# 线程池 统一管理 线程

def go(string):
    print("hello", string)
    time.sleep(random.randint(1, 4))
    return string


name_list = ["lucky", "卢yuan凯", "姚青", "刘佳俊", "何必喆"]
pool = ThreadPoolExecutor(5)  # 控制线程的并发数

all_task = [pool.submit(go, i) for i in name_list]

# 方法1：统一放入进程池使用
# print(as_completed(all_task))
for future in as_completed(all_task):
    print("finish the task")
    obj_data = future.result()
    print("obj_data is ", obj_data)

# 方法2：使用map方法获取返回值
for result in pool.map(go, name_list):
    print("task:{}".format(result))
