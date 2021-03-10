import csv
f=open("table.csv",'r')
cr=csv.reader(f)
for l in cr:
	print(l)
f.close()
up=["achu","15","mca"]
v=open("table.csv",'a')
cs=csv.writer(v)
cs.writerow(up)
v.close()
f=open("table.csv",'r')
cr=csv.reader(f)
for l in cr:
	print(l)
f.close()

