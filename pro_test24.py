# 3¹ø
def solution(h):
    max_num = 0
    for i in range(len(h)-1):
        result = 0
        for j in range(i+1,len(h)):
            if abs(i-j) == 1:
                pass
            else:
                n = j-i-1
                height = min(h[i],h[j])
                result = n*height
            if result>max_num:
                max_num=result
    return max_num


# print(solution([2,2,2,3])) # 4
print(solution([6,5,7,3,4,2])) # 12