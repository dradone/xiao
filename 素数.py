for num in range(2, 101):
    num_list = list()
    for i in range(1, num + 1):
        if num % i == 0:
            num_list.append(i)
    num_len = len(num_list)
    if num_len == 2:
        print(num)
