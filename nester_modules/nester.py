# 定义函数
# python中的递归不能超过100层

def print_lol(this_list, level=0):
 for list_each in this_list:
     if isinstance(list_each, list):
         print_lol(list_each, level+1)
     else:
         for tab in range(level):
            print("\t", end='')
         print(list_each)