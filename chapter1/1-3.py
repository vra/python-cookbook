def isAString(anobj):
    #Note suitable for UserString
    return isinstance(anobj, basestring)

def isStringLike(anobj):
    try:
        anobj.lower() + anobj + ''
    except:
        return False
    else:
        return True

if __name__ == '__main__':
    print isAString('str')
    print isAString(2)
    print isAString(u'aa')
    print isAString(str)
