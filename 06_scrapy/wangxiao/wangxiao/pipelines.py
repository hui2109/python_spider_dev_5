# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import os
from scrapy.pipelines.images import ImagesPipeline
from lxml import etree
from scrapy import Request
import urllib.parse as up


class WangxiaoPipeline:
    def __init__(self):
        self.f = None

    def process_item(self, item, spider):
        file_name = item['文件名'].replace('.', '').replace('\u3000', '')
        file_path = item['文件路径']
        question_info = item['文件内容']

        if not os.path.exists(os.path.join('../../00_素材箱/中大网校', file_path)):
            os.makedirs(os.path.join('../../00_素材箱/中大网校', file_path))

        with open(os.path.join('../../00_素材箱/中大网校', file_path, file_name + '.md'), 'a', True, 'utf-8') as f:
            f.write(question_info)
        return item


class WangxiaoImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        question_info = item['文件内容']
        tree = etree.HTML(question_info)
        srcs = tree.xpath('//img/@src')
        for _src in srcs:
            src = up.urljoin('http:', _src)
            print('src', src)
            yield Request(url=src, meta={
                "url": _src,
                "file_name": item['文件名'],
                "file_path": item['文件路径']
            })

    def file_path(self, request, response=None, info=None, *, item=None):
        _src = request.meta['url']
        file_name = request.meta['file_name']
        file_path = request.meta['file_path']
        # print(os.path.join(file_path, file_name + '_img', src.split('/')[-1]))
        return os.path.join(file_path, file_name + '_img', _src.split('/')[-1])

    def item_completed(self, results, item, info):
        # print('results', results)
        if results:  # 如果有图片下载. 才往里走
            for status, pic_info in results:
                if status:
                    http_url = pic_info['url']
                    _local_url = pic_info['path']
                    local_url = os.path.join(*_local_url.split("/")[-2:])
                    print('http_url', http_url, 'local_url', local_url)
                    item['文件内容'] = item['文件内容'].replace(http_url, local_url)
                    item['文件内容'] = item['文件内容'].replace(http_url[5:], local_url)
        return item
