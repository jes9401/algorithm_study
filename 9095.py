num=int(input())
output=[1,2,4]
for i in range(4,11):
    output.append(sum(output[-3:]))
for i in range(num):
    input_num=int(input())
    print(output[input_num-1])
