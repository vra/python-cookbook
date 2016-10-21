def count_line(filepath):
    return len(open(filepath, 'rU').readlines())

def count_line_2(filepath):
    count = -1
    for count, line in enumerate(open(filepath, 'rU')):
        pass
    count +=1
    return count

def count_line_3(filepath):
    count = 0
    thefile = open(filepath, 'rb')
    while True:
        buffer = thefile.read(8192*1024)
        if not buffer:
            break
        count += buffer.count('\n')
    thefile.close()
    return count

if __name__ == '__main__':
    print count_line('/home/yunfeng/workspace/py/python-cookbook/chapter2/2-5.py')
    print count_line_2('/home/yunfeng/workspace/py/python-cookbook/chapter2/2-5.py')
    print count_line_3('/home/yunfeng/workspace/py/python-cookbook/chapter2/2-5.py')
