max_num=0
check=0
for i in range(5):
    num=list(map(int,input().split(" ")))
    if max_num<sum(num):
        max_num=sum(num)
        check=i+1
    else:
        pass
print(check, max_num)
