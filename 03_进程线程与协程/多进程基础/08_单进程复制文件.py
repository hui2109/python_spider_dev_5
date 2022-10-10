import time


def copy_file(path, topath):
    with open(path, "rb") as fp1:
        with open(topath, "wb") as fp2:
            while 1:
                info = fp1.read(1024)
                if not info:
                    break
                else:
                    fp2.write(info)
                    fp2.flush()


if __name__ == "__main__":
    t1 = time.time()

    for i in range(1, 5):
        path = r"D:\桌面\src\%d.mp4" % i
        toPath = r"D:\桌面\des\%d.mp4" % i
        copy_file(path, toPath)

    t2 = time.time()
    # 貌似单进程复制文件更快
    print("单进程耗时：%.2f" % (t2 - t1))
