def func1(thefilepath):
    for line in open(thefilepath):
        for word in line.split():
            do_somthing_with(word)

def func2(thefilepath):
    import re
    re_word = re.compile(r"[\w'-]+")
    for line in open(thefilepath):
        for word in re_word.finditer(line):
            do_somthing_with(word)

def words_of_file(thefilepath, line_to_words=str.split):
    the_file = open(thefilepath)
    for line in the_file:
        for word in line_to_words(line):
            yield word

    the_file.close()

for word in words_of_file(thefilepath="/home/yunfeng/tmp"):
    do_somthing_with(word)

    
