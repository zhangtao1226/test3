import pymongo
client = pymongo.MongoClient(host='47.102.46.193', port=27017)

DB = client.beike
citys_coll = DB.citys
code_coll = DB.city_code
beike_citys = DB.beike_citys

citys_list = citys_coll.find().sort('_id', 1).limit(22)

citys = {}

for city in citys_list:
    list = []
    for name in city.get('city_list'):
        list.append(name)
    citys[city.get('code')] = list

print(citys)
code_list = code_coll.find()

for code in code_list:
    codeName = code.get('code')

    for key in citys.keys():
        if code.get('code') == key:
            for cl in citys[key]:
                data = {}
                data['code_id'] = code.get('_id')
                data['name'] = cl.get('name')
                data['href'] = cl.get('href')
                print(data)
                beike_citys.insert_one(data)

