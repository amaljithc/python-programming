string=input("enter a string :")
first=string[0]
string=string.replace(first,'$')
print("result is : ",first+string[1:])
