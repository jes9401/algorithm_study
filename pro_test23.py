# 부족한 금액 계산하기
def solution(price, money, count):
    answer = -1
    num = sum([(x+1)*price for x in range(count)])
    return num-money if num-money>0 else 0

print(solution(3,20,4))