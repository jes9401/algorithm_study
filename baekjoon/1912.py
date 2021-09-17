n=int(input())
random_list=list(map(int,input().split(" ")))
sum=[random_list[0]]
if n==len(random_list):
    for i in range(len(random_list)-1):
        if sum[i]+random_list[i+1]>random_list[i+1]:
            sum.append(sum[i]+random_list[i+1])
        else:
            sum.append(random_list[i+1])
print(max(sum))

