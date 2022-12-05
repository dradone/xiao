num_str = "0123456789"
print(num_str[2:6])
print(num_str[2:])
print(num_str[0:6])
print(num_str[:])
# 易错
print(num_str[1::2])
print(num_str[::2])

print(num_str[1::1])
print(num_str[2:-1])
print(num_str[-2:])
# 重点
print(num_str[::-1])