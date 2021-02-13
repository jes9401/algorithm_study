while True:
    A,B=list(map(int,input().split(" ")))
    if A<=10000 and B<=10000:
        break


a, b = A, B
while b != 0:
    a = a % b
    a, b = b, a
print(a)
print(A*B//a)
