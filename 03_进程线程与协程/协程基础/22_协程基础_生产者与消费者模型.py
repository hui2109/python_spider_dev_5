def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    r = c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s..., Current r value is %s' % (n, r))
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()

# 调用这个函数只是产生一个generator，并不能执行这个函数
# generator只能通过for循环、next()方法和send()方法执行
print(c)

produce(c)
