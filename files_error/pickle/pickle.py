# 文件存储
import pickle

new_man = []
"""
man = [1, 2, 'hello', 'world']
other = [4, 5, 'hello', 'QT']

try:
    # wb(二进制写方式打开)
    with open('man_data.txt', 'wb') as man_binary_file, open('other_data.txt', 'wb') as other_binary_file:
        pickle.dump(man, man_binary_file)
        pickle.dump(other, other_binary_file)

except pickle.PickleError as err:
    print('Pickle error!' + str(err))
"""

try:
    # wb(二进制写方式打开)
    with open('man_data.txt', 'rb') as man_binary_file, open('other_data.txt', 'rb') as other_binary_file:
        new_man = pickle.load(man_binary_file)
        pickle.load(other_binary_file)

except pickle.PickleError as err:
    print('Pickle error!' + str(err))

print(new_man)