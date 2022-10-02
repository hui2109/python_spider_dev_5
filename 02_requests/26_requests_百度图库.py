import os
import requests
import re
import urllib.request as req
import random
import time


class MyBaiduGallery:
    def __init__(self, _query_word: str, _amount: int):
        self._query_word = _query_word
        self._amount = _amount
        self.get_image_url()

    def get_image_url(self):
        self.session = requests.Session()
        self.session.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

        home_url = 'https://image.baidu.com'
        self.session.get(home_url)

        query_url = f'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word={req.quote(self._query_word)}'

        query_response = self.session.get(query_url)
        query_content = query_response.content.decode('utf-8')

        self.first_30_match_list = re.findall(r'"middleURL":"(.+?)",', query_content)
        self.first_gsm = re.findall(r"gsm: '(.+?)',", query_content)[0]

        self.remain_amount = self._amount - 30
        if self.remain_amount > 0:
            if self.remain_amount % 30 == 0:
                self.pages = self.remain_amount // 30
            else:
                self.pages = self.remain_amount // 30 + 1
        else:
            self.pages = 0

        self._get_image_data()

    def _get_image_data(self):
        self.image_data_list = []
        gsm = self.first_gsm
        for i in range(1, self.pages + 1):
            image_count = 30 * i

            data_url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10824787140586499273&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E8%B7%AF%E9%A3%9E&queryWord=%E8%B7%AF%E9%A3%9E&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={image_count}&rn=30&gsm={gsm}&1664700752783='

            data_response = self.session.get(data_url)
            data_content = data_response.content.decode('utf-8')

            match_list = re.findall(r'"middleURL":"(.+?)",', data_content)
            gsm = re.findall(r'"gsm":"(.+?)"', data_content)[0]

            self.image_data_list.extend(match_list)

        self._download_imgs()

    def _download_imgs(self):
        for j in range(self._amount):
            if j < 30:
                url = self.first_30_match_list[j]

                if not os.path.exists(f'../00_素材箱/百度文库/{self._query_word}'):
                    os.makedirs(f'../00_素材箱/百度文库/{self._query_word}')
                image_path = f'../00_素材箱/百度文库/{self._query_word}/{self._query_word}_{j + 1}.jpg'

                req.urlretrieve(url, image_path)
                print(self._query_word, '的第', f' {j + 1} ', '张图  下载完毕', sep='')
                time.sleep(random.randint(1, 5))

        if self.remain_amount > 0:
            for k in range(self.remain_amount):
                url = self.image_data_list[k]

                if not os.path.exists(f'../00_素材箱/百度文库/{self._query_word}'):
                    os.makedirs(f'../00_素材箱/百度文库/{self._query_word}')
                image_path = f'../00_素材箱/百度文库/{self._query_word}/{self._query_word}_{k + 31}.jpg'

                req.urlretrieve(url, image_path)
                print(self._query_word, '的第', f' {k + 31} ', '张图  下载完毕', sep='')
                time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    query_word = input('请输入您想下载的图片内容：')
    amount = int(input('请输入您想下载的图片数量：'))

    if amount != 0:
        mbg = MyBaiduGallery(query_word, amount)

    print('下载内容：', query_word, '，下载数量：', str(amount), '，全部下载完毕！', sep='')
