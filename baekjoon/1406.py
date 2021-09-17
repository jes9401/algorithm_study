import sys
# import time
# start_time = time.time()

text=list(sys.stdin.readline().rstrip())
n=int(sys.stdin.readline())
cursor=len(text)
start=0
end=len(text)
for i in range(n):
    command=sys.stdin.readline().rstrip()
    if command=="L" and cursor!=start:
        cursor-=1
    elif command=="D" and cursor!=end:
        cursor+=1
    elif command=="B" and cursor!=start:
        text.remove(text[cursor-1])
        cursor-=1
    elif command[0]=="P":
        text.insert(cursor,command[2])
        cursor+=1
print("".join(text))
# print("--- %s seconds ---" %(time.time() - start_time))
