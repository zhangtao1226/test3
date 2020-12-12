"""
CSV, 全称 Comma-Separated Value，中文可以叫作逗号分隔值或字符分隔值，其文件与纯文本形式存储表格数据。该文件是一个字符序列，可以由任意数目
的记录组成，记录间以某种换行符分隔。每条记录由字段组成，字段间的分隔符是其他字符或字符串，最常见的是逗号或制表符。不过所有记录都有完全相同的
字段组成序列，相当于一个结构化表的纯文本形式。
"""

import csv

def dome_write_csv():
    with open('data1.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'age'])
        writer.writerow(['001', 'tao', '20'])
        writer.writerow(['002', 'zhang', '21'])

# dome_write_csv()

def dome2_write_csv():
    with open('data2.csv', 'w') as file:
        writer =  csv.writer(file, delimiter=' ')
        writer.writerow(['id', 'name', 'age'])
        writer.writerow(['001', 'tao', '20'])
        writer.writerow(['001', 'tao', '20'])
        writer.writerow(['001', 'tao', '20'])
        writer.writerow(['001', 'tao', '20'])
        writer.writerow(['001', 'tao', '20'])
        writer.writerow(['001', 'tao', '20'])

# dome2_write_csv()


def dome_dict_write_csv():
    '''
    写入 CSV
    :return:
    '''
    with open('data3.csv', 'w') as file:
        fieldname = ['id', 'name', 'age']
        writer = csv.DictWriter(file, fieldnames=fieldname)
        writer.writeheader()
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})

# dome_dict_write_csv()

def dome_read_csv():
    '''
    读取 CSV 文件内容
    :return:
    '''
    with open('data3.csv', 'r') as file:
        reader = csv.reader(file)
        print(reader, type(reader))
        for row in reader:
            print(row)

dome_read_csv()

import pandas as pd

def dome_pandas_readCsv():
    df = pd.read_csv('data3.csv')
    print(df)

dome_pandas_readCsv()