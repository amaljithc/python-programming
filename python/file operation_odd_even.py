f1=open('odd_even.txt','r')
f2=open('odd.txt','w')
f3=open('even.txt','w')
for i in map(int,f1.readline().split()):
    if i%2!=0:
        f2.write(str(i)+' ')
    else:
        f3.write(str(i)+' ')
f1.close()
f2.close()
f3.close()