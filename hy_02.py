fd = open(r'D:\mr.txt','a+')
print("hello world",file=fd)   #注意要加 file = fd
fd.close()
