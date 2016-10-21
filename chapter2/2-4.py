import linecache
#theline = linecache.getline(thefilepath, desired_line_number)

def getline(thefilepath, desired_line_number):
    if desired_line_number < 1: return ''
    for curr_line_number, line in enumerate(open(thefilepath, 'rU')):
        if curr_line_number == desired_line_number - 1: return line
    return ''

if __name__ == '__main__':
    print getline('/home/yunfeng/workspace/py/python-cookbook/chapter2/2-3.py', 3)
