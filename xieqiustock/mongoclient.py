#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymongo
class StockMongoClient(object):
    def __init__(self,
                 host = "localhost",
                 port = 27017
                 ):
        self.con = pymongo.MongoClient(host, port)
        self.mydb = self.con.mydb
       # self.mydb.authenticate('test', 'test')
        self.stock = self.mydb.stock
        self.klinestock = self.mydb.klinestock
         
    def addStockItem(self,stockItem):
       self.stock.save({'name':stockItem["name"],
                        'symbol':stockItem["symbol"],
                        'catelog':stockItem["catelog"],
                        'market':stockItem["market"],
                        #'xq_category':stockItem["xq_category"],
                        #'zjh_category':stockItem["zjh_category"],
                        #'eps':stockItem["eps"],
                        #'pe_ttm':stockItem["pe_ttm"],
                        #'net_assets':stockItem["net_assets"],
                       # 'pb':stockItem["pb"],
                        #'rise_stop':stockItem["rise_stop"],
                        #'fall_stop':stockItem["fall_stop"],
                        #'market_capital':stockItem["market_capital"],
                        #'exchangeable_market_capital':stockItem["exchangeable_market_capital"],
                        })
    def addStockKLineDayItem(self,stockKLineDayItem):
       #self.table1.save({'name':name})
       self.klinestock.save({'symbol':stockKLineDayItem["symbol"],
                             'day':stockKLineDayItem["day"],
                             'open_price':stockKLineDayItem["open_price"],
                             'close_price':stockKLineDayItem["close_price"],
                             'low_price':stockKLineDayItem["low_price"],
                             'high_price':stockKLineDayItem["high_price"],
                             'delta_price':stockKLineDayItem["delta_price"],
                             'turn_rate':stockKLineDayItem["turn_rate"],
                             'delta_percent':stockKLineDayItem["delta_percent"],
                             'volume':stockKLineDayItem["volume"],})
       print "xx"    
       
#xx = "aaa"
#MongoClient.addName(xx) 

def main():
  stockItem =  {"name":"name1","symbol":"symbol11"} 
  StockMongoClient().addStockItem(stockItem)
if __name__ == '__main__':
  main()

 