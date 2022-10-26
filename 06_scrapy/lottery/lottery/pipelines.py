# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import pymysql


class LotteryPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(user='ahui', password='182182aA', host='43.138.31.29', port=3306, charset='utf8', database='my_test')
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()

    def process_item(self, item, spider):
        try:
            sql = 'insert into 彩票(期号, 红色球_1, 红色球_2, 红色球_3, 红色球_4, 红色球_5, 红色球_6, 蓝色球, 和值, 跨度, 区间比, 奇偶比) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            self.cursor.execute(sql, (
                item['issue'], item['red_nums'][0], item['red_nums'][1], item['red_nums'][2],
                item['red_nums'][3], item['red_nums'][4], item['red_nums'][5], item['blue_num'],
                item['sum_value'], item['span'], item['ratio'], item['odd']
            ))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        print("存储完毕")
        return item
