from pyquery import PyQuery as pq
import pymongo

html = """
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><sapn class="bold">third item</sapn></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link2.html">second item</a></li>
        </ul>
    </div>
"""

doc = pq(html)
# print(doc, type(doc))
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

li = doc('.list')
print(li.find('li'))
print(li.children(".active"))