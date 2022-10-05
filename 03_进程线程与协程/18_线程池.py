from concurrent.futures import ThreadPoolExecutor
import time


# 线程池 统一管理 线程

def go(string):
    print("hello", string)
    time.sleep(2)


name_list = ["lucky", "卢yuan凯", "姚青", "刘佳俊", "何必喆"]
pool = ThreadPoolExecutor(5)  # 控制线程的并发数

# for i in name_list:
#     pool.submit(go, i)
# 简写形式
# all_task = [pool.submit(go, i) for i in name_list]
# print(all_task)

# 统一放入进程池使用
pool.map(go, name_list)
# 多个参数
# pool.map(go, name_list1, name_list2...)
