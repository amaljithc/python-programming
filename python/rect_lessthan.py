class rectangle():
    def __init__(self, l, w):
        self.__length = l
        self.__width = w
        self.ar = self.__length * self.__width

    def __lt__(self, a2):
        if self.ar < a2.ar:
            print(self.ar, 'is least area than', a2.ar)
        else:
            print(a2.ar, 'is the least area than', self.ar)


l1 = int(input("enter the length of the first rectangle="))
w1 = int(input("enetr the width of the first rectangle="))
r1 = rectangle(l1, w1)
l2 = int(input("enter the length of the second rectangle="))
w2 = int(input("enetr the width of the second rectangle="))
r2 = rectangle(l2, w2)
r1 < r2
