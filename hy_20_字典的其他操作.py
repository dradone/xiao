name_dict = {"name": "小明",
             "age": 18}
# 统计键值对数量
print(len(name_dict))

# 合并字典
temp_dict = {"height": 1.80}
name_dict.update(temp_dict)
print(name_dict)

# 清空字典
name_dict.clear()
print(name_dict)