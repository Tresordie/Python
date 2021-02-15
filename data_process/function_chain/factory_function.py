# 定义函数对文本数据进行统一格式以便后续排序
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

# 方法串链
unique_james = []
with open("james.txt") as jaf:
    data = jaf.readline()

james = data.strip().split(',')         # 去除首尾空格
print('origin data is:')
print(james)

# filter_repeat = set(james)
# print('factory function set:')
# print(filter_repeat)
#
# print('sequence sorted:')
# print(sorted([sanitize(dat) for dat in filter_repeat], reverse=True))

# 简化代码，打印排列后集合中的前3个元素
print(sorted(set([sanitize(t) for t in james]))[0:3])
