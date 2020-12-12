a = [1, 2, 3, 4, 5, 6, 7]

newlist = filter(lambda x: x % 2 == 1, a)
newlist = [i for i in newlist]
print(newlist)