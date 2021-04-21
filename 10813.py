n,m=map(int,input().split())
dic={}
for i in range(1,n+1):
    dic.setdefault(i,i)
for j in range(m):
    temp1,temp2=map(int,input().split())
    dic[temp1],dic[temp2]=dic[temp2],dic[temp1]
for k in dic.values():
    print(k, end=" ")
