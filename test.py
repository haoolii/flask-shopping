class Demo3:
    i = 0 #類別屬性
    
    def __init__(self, i):
        self.i = i #實體屬性
        Demo3.addi2()
    
    @classmethod
    def addi(cls):
        cls.i += 1

    @staticmethod
    def addi2():
        Demo3.i += 1

d = Demo3(9531)
print(d.i)
print(Demo3.i)
Demo3.addi()
print(Demo3.i)