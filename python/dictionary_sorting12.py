dic={'rollno':8,'name':'amal','age':21,'country':'india'}
print("dictionary is : ",dic)
ascending=dict(sorted(dic.items()))
descending=dict(sorted(dic.items(),reverse=True))
print("ascending order  :",ascending)
print("descending order :",descending)
