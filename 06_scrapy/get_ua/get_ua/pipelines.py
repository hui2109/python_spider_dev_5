# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import redis


class GetUaPipeline:
    def open_spider(self, spider):
        self.r = redis.StrictRedis(host='43.138.31.29', password='182182aA', decode_responses=True)

    def close_spider(self, spider):
        self.r.save()
        self.r.close()

    def process_item(self, item, spider):
        self.r.sadd('User-Agent', item['User-Agent'])
        return item
