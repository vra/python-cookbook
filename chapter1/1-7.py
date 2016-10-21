import re
def reverse_by_char(strObj):
    return ''.join([strObj[i] for i in reversed(range(len(strObj)))])
    #Or easily,
    return strObj[::-1]
    return ''.join(reversed(strObj))

def reverse_by_word(strObj):
#    return ' '.join([strObj.split()[i] for i in reversed(range(len(strObj.split())))])
    strList = strObj.split()
    # reverse save result to itself!
    strList.reverse()
    return ' '.join(strList)

def reverse_by_word_keep_space(strObj):
    reStrObj = re.split(r'(\s+)', strObj)
    reStrObj.reverse()
    return ''.join(reStrObj)



if __name__ == '__main__':
    print reverse_by_char('hello world!')
    print reverse_by_word('hello world')
    print reverse_by_word_keep_space('  hello    world ')
