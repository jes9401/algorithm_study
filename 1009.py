t= int(input())

for i in range(t):
    a,b=map(int,input().split())
    # 반복되는 1의자리 수를 리스트에 저장
    result=[(a**x) % 10 for x in range(1,5)]
    # (b%4) -1 번째 값이 실제 결과값의 1의자리 수와 같음
    # 0~3번째이기 때
    print(result[(b%4)-1] if result[(b%4)-1]!=0 else 10)
