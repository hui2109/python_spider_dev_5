import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor, wait
from retrying import retry
import pathlib

f = open('../00_素材箱/九九电影网/ts文件目录.txt', 'r', True, 'utf-8')
ts_list = []
for line in f.readlines():
    if line.startswith('https'):
        ts_list.append(line.strip())
f.close()

session = requests.Session()
session.headers[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'


@retry(stop_max_attempt_number=3)
def download_ts_file(ts_url, index):
    t1 = time.time()
    print(f'开始下载第{index + 1}个ts文件')

    ts_response = session.get(ts_url, timeout=15)
    assert ts_response.status_code == 200

    if not os.path.exists('../00_素材箱/九九电影网/ts文件'):
        os.makedirs('../00_素材箱/九九电影网/ts文件')
    with open(f'../00_素材箱/九九电影网/ts文件/{index + 1}.ts', 'wb') as f:
        f.write(ts_response.content)

    t2 = time.time()
    print(f'第{index + 1}个ts文件下载完毕，耗时：{t2 - t1}秒')


def start_download():
    try:
        tt1 = time.time()

        pool = ThreadPoolExecutor(50)
        tasks = []

        for i in range(len(ts_list)):
            f = pool.submit(download_ts_file, ts_list[i], i)
            tasks.append(f)

        wait(tasks)

        tt2 = time.time()
        print(f'总耗时:{(tt2 - tt1):0.2f}秒')
    except Exception as e:
        print(e)


def merge(filepath, filename='output'):
    """
    进行ts文件合并，解决视频音频不同步的问题 → 建议使用这种
    """

    # 将文件的绝对路径添加到file_list中，注意不能有中文
    file_list = []
    path = pathlib.Path(filepath)
    for i in path.iterdir():
        file_list.append(str(i.absolute()))

    # 根据file_list中的文件名进行排序
    file_list = sorted(file_list, key=lambda x: int(x.split('\\')[-1].split('.')[0]))

    # 将所有ts文件名写入一个txt文件中
    with open(r'D:\exe_code\Python\ts_names.txt', 'w', True, 'utf-8') as f:
        for i in file_list:
            f.write(f"file '{i}'\n")

    # 最后，进行视频合并
    cmd = 'ffmpeg.exe -f concat -safe 0 -i D:\\exe_code\\Python\\ts_names.txt -c copy D:\\exe_code\\Python\\output.mp4'
    os.system(cmd)


if __name__ == '__main__':
    # start_download()
    merge(r'D:\exe_code\Python\ts_files')
