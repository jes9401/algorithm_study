import sys

n, score, p = list(map(int,sys.stdin.readline().rstrip().split()))
num_list = list(map(int,sys.stdin.readline().rstrip().split()))
temp = 0

if p == 0:
    print(-1)
elif n == 0:
    print(1)
else:
    num_list.append(score)
    num_list.sort(reverse=True)
    if num_list.index(score)+1 > p:
        print(-1)
    else:
        if score == num_list[-1] and n == p:
            print(-1)
        else:
            print(num_list.index(score)+1)
