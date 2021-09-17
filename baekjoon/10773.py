import sys

k = int(sys.stdin.readline())
num = []
for _ in range(k):
    n = sys.stdin.readline().rstrip()
    if n!= "0":
        num.append(int(n))
    else:
        del num[-1]
if len(num)==0:
    print(0)
else:
    print(sum(num))
