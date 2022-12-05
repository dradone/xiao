name = ["张三","李四","王五","李四"]
# len() 可以统计列表中元素的总数
name_len = len(name)
print("列表仲一共有 %d 个元素"%name_len)

# count 可以一元素在列表中出现次数
count = name.count("李四")
print("列表中含有 李四 这个元素的次数为 %d 次"%count)

# remove 会删除第一次出现的元素
name.remove("李四")
print(name)