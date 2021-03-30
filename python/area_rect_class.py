class rectangle:
    def __init__(self, l, b):
        self.len = l
        self.bred = b

    def disp(self):
        print("perimeter=", 2 * (self.len + self.bred))

    def disp1(self):
        area1 = self.len * self.bred
        print("area=", self.len * self.bred)
        return area1

    def compare(self):
        area2 = self.len * self.bred
        print("second area=", self.len * self.bred)
        return area2


def rec():
    s = rectangle(int(input("enter the length:")), int(input("enter the breadth:")))
    print("operations on rectangle \n1:area\n2:perimeter\n3:compare area\n0:exit")
    c = int(input("enter choice="))
    if c == 1:
        s.disp1()
        return rec()
    elif c == 2:
        s.disp()
        return rec()
    elif c == 0:
        print("exiting program")
        return 0
    elif c == 3:
        t = rectangle(int(input("enter the second length:")), int(input("enter the second breadth:")))
        if s.disp1() > t.compare():
            print("first area is  greater")
        else:
            print("second area is greater")
    else:
        print("invalid coice")
        return rec()


rec()