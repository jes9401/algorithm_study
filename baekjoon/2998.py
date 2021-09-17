n = input()
temp = []
result=""
dic = {'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
while len(n)>0:
    temp.append(n[-3:])
    n = n[:-3]
temp.reverse()

for i in temp:
    s = i
    if len(s) == 1:
        s = "00"+s
    elif len(s) == 2:
        s = "0"+s
    result += str(dic[s])
print(result)
        
