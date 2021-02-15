# 方法串链

with open("james.txt") as jaf:
    data = jaf.readline()
# 使用一个变量接收split之后的结果时，会将所有的元素进行分割，以列表的方式存到变量中
james = data.strip().split(',')
print(james)

# (james1, james2) = data.split(',', 1)
# print(james1)
# print(james2)
