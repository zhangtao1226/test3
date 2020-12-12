
class MemberCounter:
    members = 0
    print(id(members))
    def init(self):
        MemberCounter.members +=1


m1 = MemberCounter()
# print(id(m1))
# m1.init()

# print(MemberCounter.members)
class M2:
    members = 0
    print(id(members))
    def init(self):
        M2.members += 1

m2 = M2()

# m2 = MemberCounter()
# print(id(m2))
# m2.init()
#
# print(MemberCounter.members)