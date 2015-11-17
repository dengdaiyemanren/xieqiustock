# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from xieqiustock.items import StockItem
from xieqiustock.items import StockKLineDayItem
from xieqiustock.mongoclient import StockMongoClient

class XieqiustockPipeline(object):
    def process_item(self, item, spider):
        if type(item) != StockItem:
            return item
        #mongo_db.stocks.update({'symbol': item['symbol']}, {"$set": dict(item)}, upsert=True)
        #mongo_db.stocks.insert({'name':item["name"],'symbol':item["symbol"]})
        StockMongoClient().addStockItem(item)
        return item
    
class XieqiustockKLineDayPipeline(object):

  def process_item(self, item, spider):
    if type(item) != StockKLineDayItem:
      return item
    StockMongoClient().addStockKLineDayItem(item)
    #symbol = item['symbol']
    #sql = StockKLineDays.insert(mysql_replace_into='').values(**item)
    #with sql_engine.connect() as conn:
    #  conn.execute(sql)
    return item