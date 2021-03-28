'''
JSON ， 全称为 JavaScript Object Notation ，也就是 JavaScript 对象标记，它通过对象和数组的组合来表示数据，构造简洁但是结构化程度非常高，是一种轻量级的数据交换格式。

1、对象和数组

 * 对象 ： 使用花括号 {} 将内容包裹起来，数据结构为 {key1: value1, key2: value2, ...} 的键值对结构， 其中 key 为对象的属性，value 为对应的值。键名可以使用整数和字符串来表示。
          值的类型可以是任意类型。

 * 数组 ： 使用中括号 [] 将内容包裹起来，数据结构为 ['java', 'PHP', 'python', ....] 的索引结构。 
 
 所以 JSON 对象可以写为如下形式：
 
 [{
    'name': 'tao',
    'gender': 'male',
    'birthday': '90' 
 },{
    'name': 'zhang',
    'gender': 'male',
    'birthday': '96'
 }]

2、读取 JSON 

    Python 为我们提供了简单易用的 JSON 库来实现 JSON 文件的读写操作，我们可以调用 JSON 库的 loads() 方法将 JSON 文本字符串转为 JSON 对象，
可以通过 dumps() 方法将 JSON 对象转为文本字符串。

注 ： JSON 的数据需要用双引号包围，不能使用单引号。否则 loads() 会解析失败， 如下：
[
    {'name': 'tao'},
]
'''

import json

str = '''
[
    {"name": "tao", "gender": "male", "birthday": "90" },
    {"name": "zho", "gender": "male", "birthday": "96"}
]
'''

# print(type(str))
# data = json.loads(str)
# print(data)
# print(type(data))

def write_json():
    with open('data1.json', 'w') as file:
        file.write(json.dumps(str))

def write_json2():
    with open('data2.json', 'w') as file:
        file.write(json.dumps(str, indent=2))


write_json()
write_json2()

'''
如果出现中文，则会出现 Unicode 字符（乱码），可以指定参数 ensure_ascii = False，另外还要规定文件输出的编码：

'''

with open('filename', 'w', encoding='utf-8') as file:
    file.write(json.dumps(str, indent=2, ensure_ascii=False))
