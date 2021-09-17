n=input()
num=[0]*10
for i in n:
    num[int(i)]+=1
num[6]+=num[9]
num[9]=0
if num[6]/2==int(num[6]//2):
    num[6]=int(num[6]//2)
else:
    num[6]=int(num[6]//2)+1
num=list(set(num))
num.remove(0)
print(max(num))
