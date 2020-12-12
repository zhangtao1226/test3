class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self,size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    # size = property(get_size, set_size)

    def __setattr__(self, key, value):
        print(key,value)
        if key == 'size':
            self.width, self.height = value
        else:
            print("未找到属性")
            self.__dict__[key] = value
            print(self.__dict__)
    def __getattr__(self, item):
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError()


r = Rectangle()
r.size = 10,29
# r.height = 20
#
# print(r.size)
#
# r.siza = 100, 30
#
# print(r.width, r.height)