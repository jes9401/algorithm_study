import sys
import bisect
n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().rstrip().split()))
result=[A[0]] # 첫번째 값이 저장된 result 리스트 생성
for i in range(1,n):
    if A[i]>result[-1]: # 최대값보다 클 경우
        result.append(A[i]) # result에 추가
    else:
        temp = bisect.bisect_left(result,A[i])
        # bisect_left
        # => 정렬된 순서 유지되도록
        # result에 A[i]를 삽입할 위치
        result[temp]=A[i]
print(len(result))