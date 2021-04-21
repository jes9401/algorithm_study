student, max_student = map(int,input().split())

dic_f={}
dic_m={}
room=0
for i in range(student):
    s,y=map(int,input().split())
    if s==0:
        if y in dic_f:
            dic_f[y]+=1
        else:
            dic_f.setdefault(y,1)
    else:
        if y in dic_m:
            dic_m[y]+=1
        else:
            dic_m.setdefault(y,1)
for j in dic_f:
    if dic_f[j]<max_student:
        room+=1
    elif dic_f[j]%max_student==0:
        room+= (dic_f[j]//max_student)
    else:
        room+= (dic_f[j]//max_student)+1

for k in dic_m:
    if dic_m[k]<max_student:
        room+=1
    elif dic_m[k]%max_student==0:
        room+= (dic_m[k]//max_student)
    else:
        room+= (dic_m[k]//max_student)+1

print(room)
