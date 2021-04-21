import sys

# 공격력, 힘, 치명타 확률, 치명타 피해비율, 공속 증가


def power(lst):
    result = min(20000,lst[0])*(1+(min(20000,lst[1])/100))*(1+lst[4])*((1-min(lst[2],1))+min(lst[2],1)*lst[3])
    return result


c1 = list(map(int, input().split()))
p1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
p2 = list(map(int, input().split()))

c_p = []
p_c = []
for i in range(len(c1)):
    c_p.append(c1[i]-c2[i]+p2[i])
    p_c.append(p1[i]-p2[i]+c2[i])


