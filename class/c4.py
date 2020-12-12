class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Asssss")
            self.hungry = False
        else:
            print("No,thanks!")

class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk'
    def sing(self):
        print(self.sound)
    def eat(self):
        print("sub Class")
class ThirdSub(SongBird):
    def __init__(self):
        super().__init__()
        self.name = 'tao'
    def eat(self):
        print('zhang')

sb = SongBird()

sb.sing()
sb.eat()

th = ThirdSub()
th.eat()
print(th.hungry, th.sound)