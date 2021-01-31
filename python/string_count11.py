string=input("enter the text :")
string=string.lower()
l1=string.split()
l2=list(set(l1))
for i in l2 :
    print(i,"=",l1.count(i))
