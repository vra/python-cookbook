import itertools
import os
def anyTrue(predicate, sequence):
    return True in itertools.imap(predicate, sequence)
def is_endwith(s, *ends):
    return anyTrue(s.endswith, ends)



if __name__ == '__main__':
    print is_endwith('hello world', 'd', 'a', 'b')
    # example: find image file in dir
    for filename in os.listdir('.'):
        if is_endwith(filename, '.jpg', '.png', '.jpeg', '.gif'):
            print filename
    #Bound Method example
    l = ['apple', 'grape', 'banana']
    x = l.append
    x('pie') # equals to l.append('pie')
    list_x = list.append
    list_x(l, 'pie') # equals to operator above
    
