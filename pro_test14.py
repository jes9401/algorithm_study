# 프로그래머스 
# 핸드폰 번호 가리기  https://programmers.co.kr/learn/courses/30/lessons/12948


def solution(phone_number):
    return phone_number.replace(phone_number[:-4],"*"*len(phone_number[:-4]))
