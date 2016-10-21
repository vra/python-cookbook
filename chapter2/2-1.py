#File reading
#1 .Read All content
all_the_text = open('name.txt', 'rU').read() #'rU' will tran `\n\r`, '\r' to '\njj'
all_the_data = open('abinfile', 'rb').read()

# Read with try-finally
file_object = open('thefile.txt')
try:
    all_the_text = file_object.read()
finally:
    file_object.close()

#Read by line
list_of_all_the_line = file_object.readlines()
list_of_all_the_line = file_object.read().splitline() #remove `\n` at the end
list_of_all_the_line = file_object.read().split('\n') # remove "\n" at the end
list_of_all_the_line = [L.rstrip('\n') for L in file_object ]
for line in file_object:
    # line = line.rstrip()
    process(line)
