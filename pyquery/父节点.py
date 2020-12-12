'''
parent() 方法获取父节点
parents() 方法获取祖先节点
'''

html = '''
    <div class="wrap">
        <div id="container">
            <ul class="list">
                <li class="item-0">first item</li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <li class="item-0 active"><a href="link3.html"><sapn class="bold">third item</sapn></a></li>
                <li class="item-1 active"><a href="link4.html">fourth item</a></li>
                <li class="item-0"><a href="link2.html">second item</a></li>
            </ul>
        </div>
    </div>
'''

from pyquery import PyQuery as pyq
doc = pyq(html)
items = doc('.list li').items()


for item in items:
    print(item.attr("class"))
