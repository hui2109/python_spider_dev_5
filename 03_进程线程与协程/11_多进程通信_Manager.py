import multiprocessing


def fun(mydict, mylist):
    # print(mylist)
    mydict['x'] = 'x'
    mydict['y'] = 'y'
    mydict['z'] = 'z'

    mylist.append('12')
    mylist.append('34')
    mylist.append('56')


if __name__ == '__main__':
    # Manager是一种较为高级的多进程通信方式，它能支持Python支持的的任何数据结构。
    mydict = multiprocessing.Manager().dict()
    mylist = multiprocessing.Manager().list()
    p = multiprocessing.Process(target=fun, args=(mydict, mylist))
    p.start()
    p.join()
    print(mydict)
    print(mylist)
