num=int(input())
num1=num
i=0
if 0<=num1<=99:
    while True:
        if num1<10:
            num1=(num1*10)+num1
            i+=1
        else:
            num1= ((num1%10)*10)+ ((num1//10 + num1%10)%10)
            i+=1
        if num1==num:
            break
print(i)
