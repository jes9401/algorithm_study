N=int(input())
num_list=input().split(" ")
result=0

if N==len(num_list):
    for i in range(len(num_list)):
        count=0
        for j in range(1, int(num_list[i])+1):
            if int(num_list[i])%j==0:
                count+=1
        if count==2:
            result+=1
        
print(result)
