def pyramid(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j*i,end=" ")
        print("\n")
n=int(input("enter the limit :"))
pyramid(n)
