import sys

def command(s,l):
    result.append(s.split()[1])
    return result
def command2(s,l):
    if s=="pop":
        return -1 if len(l)==0 else l.pop(0)
    elif s=="size":
        return len(l)
    elif s=="empty":
        return 1 if len(l)==0 else 0
    elif s=="front":
        return -1 if len(l)==0 else l[0]
    elif s=="back":
        return -1 if len(l)==0 else l[-1]


result=[]
n=int(input())

for i in range(n):
    text=sys.stdin.readline().rstrip()
    if " " in text:
        result=command(text,result)
    else:
        print(command2(text,result))
