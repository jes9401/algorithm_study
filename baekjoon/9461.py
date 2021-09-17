def get_data(n):
    num_list = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n<=10:
        return num_list[n-1]
    else:
        while n>len(num_list):
            num_list.append(num_list[-2]+num_list[-3])
        return num_list[-1]
        
n = int(input())
for i in range(n):
    input_num = int(input())
    result = get_data(input_num)
    print(result)
