import sys

input_str = list(sys.stdin.readline().rstrip())
input_str.sort(reverse=True)
count_dict = {}
temp = 0
result = ""
center = ""
for i in input_str:
    if i in count_dict:
        count_dict[i]+=1
    else:
        count_dict.setdefault(i,1)
for j in count_dict:
    if count_dict[j]%2 != 0:
        temp +=1
        center = j
    if temp>1:
        result = "I'm Sorry Hansoo"
        break
if temp<=1:
    if temp == 0:
        for x in count_dict:
            for y in range(count_dict[x]//2):
                result = x+result+x
        print(result)
    else:
        count_dict[center]-=1
        result = center
        for x in count_dict:
            for y in range(count_dict[x]//2):
                result = x+result+x
        print(result)
else:
    print(result)