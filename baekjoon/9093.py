n=int(input())

for i in range(n):
    text=input().split()
    for j in range(len(text)):
        if j<len(text)-1:
            print(text[j][::-1],end=" ")
        else:
            print(text[j][::-1])
