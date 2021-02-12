# 文件存储
import sys

def print_lol_fileformat(this_list, indent=False, level=0, fn=sys.stdout):
    for list_each in this_list:
        if isinstance(list_each, list):
            print_lol_fileformat(list_each, indent, level+1, fn)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='')
            print(list_each, file=fn)

man = []
other = []

try:
    data = open("sketch.txt")
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()           # 去掉字符串中的空白符
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

try:
    with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
        print_lol_fileformat(man, fn=man_file)          # 将列表输出到那个文件中
        print_lol_fileformat(other, fn=other_file)

except IOError as err:
    print('File error!' + str(err))
