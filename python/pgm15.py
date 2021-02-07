def fact(n):
    f=1
    if n==0:
       print("factorial is :",f)
    else:
        for i in range(1,n+1):
            f=i*f
        print("factorial is :",f)
n=int(input("enter a number :"))
fact(n)
