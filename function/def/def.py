# 定义函数
# python中的递归不能超过100层

def print_lol(this_list):
    for list_each in this_list:
        if isinstance(list_each, list):
            print_lol(list_each)
        else:
            print(list_each)

movies = ["hello1", "hello2", 'hello3', ['hello5', 1978, "hello6", [123, 'hello7']]]
print_lol(movies)
