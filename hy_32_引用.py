def text(num):
    print("数学 %d 所在的内存地址为 %d " % (num, id(num)))
    result = "hello"
    print("数据在内存中保存的地址为 %d " % id(result))
    return result


a = 1
print("数学a所保存的数据在内存中的地址为 %d " % a)
r = text(a)
print("%s 在内存中保存的地址为 %d" % (r, id(r)))
