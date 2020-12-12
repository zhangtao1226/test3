import json

a = 'this is test write'

def write_test(content):
    with open('test.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+ '\n')


for i in range(10):
    write_test(a)