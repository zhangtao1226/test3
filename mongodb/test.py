import pymongo

client = pymongo.MongoClient(host='47.102.46.193', port=27017)

db = client.beike

mycol = db.citys


data = mycol.find({}, {'code': 1})
print(data)

for d in data:
    print(d)
