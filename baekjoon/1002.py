n = int(input())


# 1. 두 원이 일치하는 경우 => 무수히 많다 => -1 리턴
# 두 점 사이의 거리가 0 => r=0
# 거리가 같다 => r1=r2

# 2. 가장 큰 거리가 나머지 두 개의 합이 같다 => 한 점에서 만남(내접or외접) => 1리턴
# maxR=sum(R) 인 경우 or r=r1+r2 인 경우

# 3. 가장 큰 값이 나머지 두 개의 합보다 큰 경우 => 안 만남 => 0리턴
# maxR>sum(R)

# 그 외에 경우 2개의 점에서 만남 => 2 리턴
for i in range(n):
    x1,y1,r1,x2,y2,r2=list(map(int,input().split()))
    r= (((x1-x2)**2)+((y1-y2)**2))**(1/2)
    R=[r1,r2,r]
    result=None
    maxR=max(R)
    R.remove(maxR)
    if r==0 and r1==r2:
        result=-1
    elif maxR==sum(R):
        result=1
    elif maxR>sum(R):
        result=0
    else:
        result=2
    print(result)
