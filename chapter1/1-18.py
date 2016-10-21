import re

def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

#closure
def make_xlat(*arg, **kwds):
    adict = dict(*arg, **kwds)
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    def xlat(text):
        return rx.sub(one_xlat, text)
    return xlat

class make_xlat:
    def __init__(self, *args ,**kwds):
        self.adict = dict(*args, **kwds)
        self.rx = self.make_rx()
    def make_rx(self):
        return re.compile('|'.join(map(re.escape, self.adict)))
    def one_xlat(self, match):
        return self.adict[match.group(0)]
    def __call__(self, text):
        return self.rx.sub(self.one_xlat, text)

class make_xlat_by_whole_words(make_xlat):
    def make_rx(self):
        return re.compile(r'\b%s\b'% r'\b|\b'.join(map(re.escape, self.adict)))

if __name__ == '__main__':
#    print multiple_replace('hello world', {'hello':'bye'})
    my_xlat = make_xlat({'hello': 'by'})
    print my_xlat('hello world')
    mx = make_xlat({'hello':'bye'})
    print mx('hello world')
    mx_whole = make_xlat_by_whole_words({'hello':'world'})
    print mx_whole('hello world')
