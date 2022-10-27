# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import Request
# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline


class ZolPicturePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        src = item['src']
        yield Request(src, meta={'info': src})

    def file_path(self, request, response=None, info=None, *, item=None):
        src = request.meta['info']
        file_name = src.split('/')[-1]
        return f'zol_pictures/{file_name}'

    def item_completed(self, results, item, info):
        return item
