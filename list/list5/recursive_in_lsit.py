# 多层嵌套列表递归打印

movies = ["hello1", "hello2", 'hello3', ['hello5', 1978, "hello6", [123, 'hello7']]]
print("print all members in list")
print(movies)

print("for list_each print")
for list_each in movies:
    if isinstance(list_each, list):             # 判断列表内元素是否是列表
        for nested_list in list_each:
            print(nested_list)
    else:
        print(list_each)

