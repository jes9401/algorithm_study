E,S,M,count =1,1,1,1

E1,S1,M1 = map(int,input().split())

while(True):
    if E1==E and S1==S and M1==M :
        break
    E+=1
    S+=1
    M+=1
    count+=1
    if E>=16 : E-=15
    if S>=29 : S-=28
    if M>=20 : M-=19
print(count)
