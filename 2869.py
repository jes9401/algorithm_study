A,B,V=map(int,input().split(" "))

i=(V-B)/(A-B)
if int(i)==i:
    print(int(i))
else:
    print(int(i)+1)
