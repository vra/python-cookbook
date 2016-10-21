import string

def translator(frm='', to='', delete='', keep=None):
    if len(to) == 1:
        to = to * len(frm)

    trans = string.maketrans(frm, to)
    if keep is not None:
        allchar = string.maketrans('', '')
        delete = allchar.translate(allchar, keep.translate(allchar, delete))
    def translate(s):
        return s.translate(trans, delete)
    return translate

if __name__ == '__main__':
    up = translator('a', 'A')
    print up('abcd')
