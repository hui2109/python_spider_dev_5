import flask

from save_ip import HSaveIp

web_app = flask.Flask(__name__)

redis = HSaveIp()


@web_app.route('/')
def get_available_ip():
    ip = redis.zset_getip()
    if ip:
        return ip
    else:
        print('暂时没有可用的ip')


def main():
    # 开启debug模式后，main.py不能正常运行
    web_app.run()


if __name__ == '__main__':
    main()
