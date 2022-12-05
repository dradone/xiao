poem = "小池\t杨万里\n泉眼无声惜细流，\t\t树阴照水爱晴柔。\t小荷才露尖尖角\t\n早有蜻蜓立上头。"
print(poem)
# 拆分字符串
poem_list = poem.split()
print(poem_list)
# 合并字符串
result = " ".join(poem_list)
print(result)