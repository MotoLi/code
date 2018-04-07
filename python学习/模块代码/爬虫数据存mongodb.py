# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import sys
import unittest
reload(sys)
sys.setdefaultencoding('utf-8')
class MongoAPI(object):
    def __init__(self, db_ip, db_port, db_name, table_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.table_name = table_name
        self.conn = pymongo.MongoClient(host=self.db_ip, port=self.db_port)
        self.db = self.conn[self.db_name]
        self.table = self.db[self.table_name]
    def get_one(self, query):
        return self.table.find_one(query, projection={"_id": False})
    def get_all(self, query):
        return self.table.find(query)
    def add(self, kv_dict):
        return self.table.insert(kv_dict)
    def delete(self, query):
        return self.table.delete_many(query)
    def check_exist(self, query):
        ret = self.get(query)
        return len(ret) > 0
    # 如果没有 会新建
    def update(self, query, kv_dict):
        ret = self.table.update_many(
            query,
            {
                "$set": kv_dict,
            }
        )
        if not ret.matched_count or ret.matched_count == 0:
            self.add(kv_dict)
        elif ret.matched_count and ret.matched_count > 1:
            self.delete(query)
            self.add(kv_dict)
class DBAPITest(unittest.TestCase):
    def setUp(self):
        self.db_api = MongoAPI("127.0.0.1",  # 图书馆大楼地址
                                27017,  # 图书馆门牌号
                                "test",  # 一号图书室
                                "test_table")  # 第一排书架
    def test(self):
        db_api = self.db_api
        db_api.add({"url": "test_url", "k": "v"})
        self.assertEqual(db_api.get_one({"url": "test_url"})["k"], "v")
        db_api.update({"url": "test_url"}, {"url_update": "url_update"})
        ob = db_api.get_one({"url": "test_url"})
        self.assertEqual(ob["url_update"], "url_update")
        db_api.delete({"url": "test_url"})
        self.assertEqual(db_api.get_one({"url": "test_url"}), None)
if __name__ == '__main__':
    unittest.main()