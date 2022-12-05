# 判断空白字符串
str_1 = "  \t\n"
print(str_1.isspace())

# 判断字符串是否只含有数字
# 三种方法都不能判断小数
num_str = "1"
print(num_str.isdecimal())
# 可以输入特别的数字
print(num_str.isdigit())
# 可以输出中文数字
print(num_str.isnumeric())