# 增加更多的数据
# 1.列表的Insert方法
# 2.处理列表数据
# 3.转义字符
# 4.列表中的存储列表

movies = ['The Holy Grail', "The Life of Brian", 'The Meaning of Life']
world = ["maya", 1957, "hanmeimei", 1986, "jinlei", 1864,
         ["lilei", "john",
          ["tk", "sk", "my"]]]

movies.insert(0, "FuckU")
print(movies)

movies.insert(0, "\"\"")
print(movies)

for fac_movie in movies:
    print(fac_movie)

print(world)