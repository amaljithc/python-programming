a=int(input("enter first number :"))
b=int(input("enter second number :"))
while(b!=0):
    t=b
    b=a%b
    a= t   
print(a)
