import pymongo
client = pymongo.MongoClient(host='47.102.46.193', port=27017)
db = client.douban
tag_list = []

with open('豆瓣图书标签类型', 'r') as file:
    tag_list = file.read().strip('[]').strip("'").split("', '")

for tag in tag_list:
    tag_dict = {}
    tag_dict['tag_name'] = tag
    tag_dict['tag_type'] = 1
    tag_dict['tag_from'] = 1
    result = db.tag_type.insert_one(tag_dict)


