# 文件基本操作：打开文件，处理文件，关闭文件
import os
os.getcwd()
os.chdir('../fileIO')
the_file = open("sketch.txt", 'r')

for line_each in the_file:
    if not line_each.find(":") == -1:
        (role, line_spoken) = line_each.split(":", 1)
        print(role, end='=>')
        print(line_spoken, end='')

the_file.close()

"""
# split用法
line_content = the_file.readline()
(role, line_spoken) = line_content.split(":")
print(role, end='\n')
print(line_spoken, end='\n')
"""

"""
# readline用法
for line_each in the_file:
    line_content = the_file.readline()
    print(line_content, end='')
"""
"""
# seek()用法
line_content = the_file.readline()
print(line_content, end='')

line_content = the_file.readline()
print(line_content, end='')
the_file.seek(0)
line_content = the_file.readline()
print(line_content, end='')
"""


