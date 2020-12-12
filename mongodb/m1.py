import pymongo

client = pymongo.MongoClient(host='47.102.46.193', port=27017)

db = client.scrapy_test

print(db)



