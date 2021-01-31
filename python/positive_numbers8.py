n=input("enter numbers : ")
l1=[int(i) for i in n.split()]
l2=[i for i in l1 if i>0]
print("enterd list of numbers is",l1)
print("positive numbers is =",l2)
