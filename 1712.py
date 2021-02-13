A,B,C=map(int,input().split(" "))
i=0
if C<=B:
    i=-1
else:
    i=A//(C-B)+1
print(i)
