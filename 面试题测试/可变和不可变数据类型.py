
a = 1   # id = 4322139312
b = 2   # id = 4322139344
c = 3   # id = 4322139376

d = [1, 2, 3]   # id = 140328593475784; [4322139312, 4322139344, 4322139376]

print(id(a), id(b), id(c))
print(id(d))
for i in d:
    print(id(i))