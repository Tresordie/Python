# python的列表有哪些方法
# 1.列表末尾增加一个数据项             append
# 2.列表末尾删除数据                  pop
# 3.列表末尾增加一个数据项集合          extend(其将extend中的数据项集合中的数据拼接到列表的后面)
# 4.列表中找到并删除一个特定的数据项     remove
# 5.列表中的长度                     len
# 6.列表中某个特定位置前增加一个数据项   insert


movies = ['The Holy Grail', "The Life of Brian", 'The Meaning of Life']
print(movies)
print("the length of list is:", len(movies))

movies.append("Mountain Tower")
print(movies)

movies.pop()
print(movies)

movies.extend(["Good News", "Good Days"])
print(movies)
print(len(movies))

movies.remove("The Holy Grail")
print(movies)

movies.insert(0, "FuckU")
print(movies)
