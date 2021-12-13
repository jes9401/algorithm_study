from itertools import combinations
nums=[i for i in range(10)]
result=[]
for i in range(1,11):
    temp=list(combinations(nums,i))
    for j in temp:
        result.append(int(''.join(sorted(map(lambda x:str(x), j), reverse=True))))
result.sort()

n = int(input())
print(-1) if n>=1024 else print(int(result[n-1]))
