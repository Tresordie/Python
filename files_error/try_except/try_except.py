# encoding=UTF-8
# 打开文件时，如果文件不存在会出现IOError
try:
    the_file = open("sketch.txt", 'r')

except IOError as err:
    print("File error" + str(err))

# the_file的名字存在说明打开文件成功，否则打开失败
if 'the_file' in locals():
    the_file.close()


