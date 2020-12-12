from urllib.request import urlopen
import re
webpage = urlopen('file:///Users/zhangtao/Desktop/t.html')
text = webpage.read()
print(str(text, encoding = "utf-8"))  #bytes 转str