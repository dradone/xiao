poem = ["小池",
"杨万里",
"泉眼无声惜细流，\t\n",
"\t树阴照水爱晴柔。",
"\n小荷才露尖尖角，",
"早有蜻蜓立上头。"]
for poem_str in poem:
    #print("|%s|"%poem_str.center(10))
    #print("|%s|" % poem_str.ljust(10))
    #print("|%s|" % poem_str.rjust(10))
    print("|%s|"%poem_str.strip().center(10))
