name_dict = {"name": "小明"}
# 取值
print(name_dict["name"])

# 增加和修改
name_dict["age"] = 18
name_dict["name"] = "小红"
print(name_dict)

# 删除
name_dict.pop("name")
print(name_dict)