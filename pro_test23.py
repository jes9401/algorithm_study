# 1¹ø
def solution(n):
    temp =[]
    for i in range(1,n):
        temp.append((n*i)+i)
    return sum(temp)


print(solution(2)) # 3
print(solution(3)) # 12