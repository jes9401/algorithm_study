n,k= map(int,input().split())

temp=[x for x in range(1,n+1)]
result=[]
# 1,2,3,4,5,6,7 일때
# k번째 추출 후 k+1번째부터 반복
while len(temp)>0:
    if len(temp)<k:
        if len(temp)==1:
            result.append(temp.pop(0))
        else:
            num=(k%len(temp))
            if num==0:
                result.append(temp.pop(-1))
            else:
                result.append(temp.pop(num-1))
                temp=temp[num-1:]+temp[:num-1]
    else:
        result.append(temp.pop(k-1))
        temp=temp[k-1:]+temp[:k-1]
result=list(map(str,result))
print("<"+", ".join(result)+">")
