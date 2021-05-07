temp = 10

while temp!=0:
    result = 2
    temp = int(input())
    if temp == 0:
        break
    else:
        num = str(temp)
        for i in num:
            if i == "0":
                result+=4
            elif i == "1":
                result+=2
            else:
                result+=3
        print(result+len(num)-1)
