#!/usr/bin/env python
# -*- coding: utf-8 -*-


#from pymongo import MongoClient
import  pymongo

MONGODB_URI = 'mongodb://192.168.236.131:27017/mydb' 
SEED_DATA = [
    {
        'decade': '1970s',
        'artist': 'Debby Boone',
        'song': 'You Light Up My Life',
        'weeksAtOne': 10
    },
    {
        'decade': '1980s',
        'artist': 'Olivia Newton-John',
        'song': 'Physical',
        'weeksAtOne': 10
    },
    {
        'decade': '1990s',
        'artist': 'Mariah Carey',
        'song': 'One Sweet Day',
        'weeksAtOne': 16
    }
]

class CommonMongoClient(object):
    def __init__(self,table):
        self.client =  pymongo.MongoClient(MONGODB_URI)
        self.db = self.client.get_default_database()
        self.table = self.db[table]
    def count(self,cond):
         return self.table.find(cond).count()
    def query(self,cond,sort):
        return self.table.find(cond).sort(sort)
    def update(self,cond,context):
        self.table.update(cond,context)
    def insert(self,context):
        self.table.insert(context); 
    def delete(self,cond):
        self.table.remove(cond)
        
def main():
    queryCondA = {"catelog":"A股"}
    #cursor =  CommonMongoClient("stock").query(queryCondA,"symbol")
    #print cursor
    CommonMongoClient("SEED").insert(SEED_DATA)
    
    result = CommonMongoClient("SEED").query({"decade":"1990s"},"decade")

    for i in result:
        print i
    #CommonMongoClient("SEED").delete({"decade":"1990s"})

    
   # CommonMongoClient("stock").table.update(queryCondA,);
     
    #print CommonMongoClient("klinestock").table.find().count()  
    
    
if __name__ == '__main__':
    main()