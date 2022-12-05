def print_xxx(char,times):
    print(char * times)


def print_lines(char,times):
    row = 0
    while row < 5:
        print_xxx(char,times)
        row += 1


print_lines("_",50)