import pymongo

client = pymongo.MongoClient(host='47.102.46.193', port=27017)

db = client.beike
coll = db.city_code_en
newColl = db.city_code

code_list = []

city_codes = coll.find().sort('_id', 1).limit(22)

for code in city_codes:
    # print(code)
    code_list.append(code.get("code"))

for code in code_list:
    d = {}
    d['code'] = code
    result = newColl.insert_one(d)