class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self, item):
        self.counter += 1
        return super(CounterList, self).__getitem__(item)


c1 = CounterList(range(10))

print(c1)

c1.reverse()

print(c1)

del c1[2:4]

print(c1)

print(c1.counter)
c1[3] + c1[5]

print(c1.counter)