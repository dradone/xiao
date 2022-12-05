name = ["zhangsan","lisi","wangwu"]
#1. 取值和取索引
print(name[2])
# index 可以看到数据所在索引位置
print(name.index("lisi"))

#2. 修改
#注意 ”[]“ 里填的是对应的索引
name [1] = "李四"
print(name)

#3. 增加
# append 可以在列表末尾追加一个数据
name.append("靓仔")
# insert 可以在索引内加入需要的元素
name.insert(2,"靓女")
# extend 可以加入一个其他的列表
temp_list = ["孙悟空","猪八戒","沙师弟"]
name.extend(temp_list)
print(name)

#4. 删除

# pop 默认时将删掉最后一个数据
name.pop()
# pop 可以删除指定索引的输据
name.pop(2)
# remove 可以删除指定数据
name.remove("靓仔")
# clear 可以清空列表
name.clear()
print(name)