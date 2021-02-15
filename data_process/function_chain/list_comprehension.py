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
clean_james = []

with open("james.txt") as jaf:
    data = jaf.readline()
# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
# 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
# 1. 使用一个变量接收split之后的结果时，会将所有的元素进行分割，以列表的方式存到变量中
james = data.strip().split(',')         # 去除首尾空格
print("firstly split from text:")
print(james)
# 2. 列表推导方式简化代码
# clean_james = [sanitize(dat) for dat in james]
# print("second split to format data:")
# print(clean_james)
# # 3. 数据复制排序
# print("finally to sorted data and output:")
# print(sorted(clean_james))
print(sorted([sanitize(dat) for dat in james]))
