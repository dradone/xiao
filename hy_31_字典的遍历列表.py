students = [{"name":"王小二"},{"name":"小明"}]
find_name = "小红"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s"%find_name)
        break
else:
    print("没找到 %s 这个人！"%find_name)
print("循环结束！")