# key words to extract the coordinate
str_start = "[ss_batt_do_sample][ss_bat]UI sample "
str_end   = ","

f_orig = open('I:/Projects/python/keyword/batt.csv') # original file

f_coord = open('I:/Projects/python/keyword/gen.csv', 'w')  # target file used to save

line = f_orig.readline()
while line:

    # find index according to the key words
    index_start = line.find(str_start)
    index_end = line.find(str_end)
    text = line[index_start : index_end]

    if text != '':
        # If there is more than one [], we can use "Coordinate" and "End" as str_start and str_end
        # f_coord.write(str(line[index_start + 1 : index_end]) + '\n')
        f_coord.write(str(line[11:16]) + "," + str(line[(index_end - 3) : index_end]) + '\n')

    line = f_orig.readline()

f_orig.close()
f_coord.close()