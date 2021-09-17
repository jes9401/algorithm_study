n = int(input())
young = ""
young_date = [1989,1,1]
old = ""
old_date = [2011,12,31]
dic = {}
for i in range(n):
    temp = input().split()
    name = temp[0]
    birth = temp[::-1][:-1]
    birth = list(map(int,birth))
    dic.setdefault(name,birth)
for j in dic:
    if dic[j][0]>young_date[0]:
        young_date = dic[j]
        young = j
    elif dic[j][0] == young_date[0]:
        if dic[j][1]>young_date[1]:
            young_date = dic[j]
            young = j
        elif dic[j][1] == young_date[1]:
            if dic[j][2]>young_date[2]:
                young_date = dic[j]
                young = j


for k in dic:
    if dic[k][0]<old_date[0]:
        old_date = dic[k]
        old = k
    elif dic[k][0] == old_date[0]:
        if dic[k][1]<old_date[1]:
            old_date = dic[k]
            old = k
        elif dic[k][1] == old_date[1]:
            if dic[k][2]<old_date[2]:
                old_date = dic[k]
                old = k

print(young)
print(old)