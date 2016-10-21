def replace_substr(strObj, replaceDict):
    #replaceDict:{'abc':'def', 'mn': 'xy'}
    for key,value in replaceDict.iteritems():
        if key in strObj:
            strObj = strObj.replace(key, value)
    return strObj

if __name__ == '__main__':
    print replace_substr("abc mn ", {"abc": "def", "mn": "xy"})
