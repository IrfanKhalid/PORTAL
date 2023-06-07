# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import sys
from .items import Jobs

class Ins2Pipeline:
    
    collection ='scrapy_items'
    
    def __init__(self):
        print("Do Nothing")        
    @classmethod
    # def from_crawler(cls,crawler):
    #     return cls(
    #         mongodb_uri=crawler.settings.get('MONGODB_URI'),
    #         mongodb=crawler.settings.get('MONGODB_DATABASE','items')                    
    #     )
        
    def open_spider(self,spider):
        self.client=pymongo.MongoClient("mongodb+srv://crawl:adax1234@cluster0.ri9k69r.mongodb.net/?retryWrites=true&w=majority")
        self.db=self.client["jobs"]
        #Start with a clean database
        self.db[self.collection].delete_many({})
        
    def close_spider(self,spider):
        self.client.close()
        
    def process_item(self, item,spider):
        data=dict(Jobs(item))
        self.db[self.collection].insert_one(data)
        return item