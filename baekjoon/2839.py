while True:
    num=int(input())
    if 3<=num<=5000:
        break
result=0
while True:
    if num%5==0:
        result+=num//5
        break
    num-=3
    result+=1
    if num<0:
        result=-1
        break
print(result)
