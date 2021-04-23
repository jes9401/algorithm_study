a,b= input().split()
a=list(a)
b=list(b)
count=0
temp=51
#idx=0
for i in range(len(b)-len(a)+1):
    b2=b[i:len(a)+i]
    count=0
    for j in range(len(b2)):
        if a[j]!=b2[j]:
            count+=1
    if count<temp:
        temp=count
 #       idx=b2
print(temp)
#print(idx)
    
