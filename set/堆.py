from heapq import *
from random import shuffle

# data = list(range(10))
# # print(data)
# shuffle(data)
# heap = []
#
# for i in data:
#     # print(i)
#     heappush(heap, i)
#
# print(type(nlargest(3, heap)))

list = [1, 3, 4, 6, 7]
heapify(list)

print(type(list))
heappush(list, 11)
print(list)
heappop(list)
print(list)

print(nlargest(2, list))
print(list)
print(nsmallest(3, list))
print(list)
heapreplace()




