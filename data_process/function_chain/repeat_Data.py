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

for each_data in james:
    if each_data not in unique_james:
        unique_james.append(each_data)
print('filter repeat data:')
print(unique_james)
print('sequence sorted:')
print(sorted([sanitize(dat) for dat in unique_james], reverse=True))