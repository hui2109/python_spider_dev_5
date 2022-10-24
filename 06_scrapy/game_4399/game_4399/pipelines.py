# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class Game4399Pipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(user='ahui', password='182182aA', host='43.138.31.29', port=3306, charset='utf8', database='my_test')
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()

    def process_item(self, item, spider):
        try:
            sql = 'insert into 4399游戏库(游戏名称, 游戏类型, 游戏创建时间) values (%s, %s, %s)'
            self.cursor.execute(sql, (item['游戏名'], item['游戏类型'], item['游戏时间']))
            self.db.commit()
            spider.logger.info(f"保存数据【{item}】")
        except Exception as e:
            self.db.rollback()
            # 记录错误日志
            spider.logger.error(f"保存数据库失败!", e, f"数据是: {item}")
        return item
