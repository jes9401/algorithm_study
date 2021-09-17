n = int(input())
f = int(input())
result = 0

n2 = n - n%100
for i in range(n2, n2+101):
    if i % f ==0:
        result=i
        break
print(str(result)[-2:])
