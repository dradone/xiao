for i in range(1000):
    i += 1
    sum_1 = 0
    num_list = list()

    for num in range(i):
        num += 1
        if i % num == 0:
            num_list.append(num)
    for a in num_list:
        sum_1 += a
    sum_2 = sum_1 - i
    if sum_2 == i:
        print(i)
