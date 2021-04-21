s=input()
temp=[]
text=""
i=0
if "<" not in s and ">" not in s:
    s=s.split()
    for i in range(len(s)):
        if i<len(s):
            print(s[i][::-1],end=" ")
        else:
            print(s[i][::-1])
else:
    while len(s)>0:
        pass
