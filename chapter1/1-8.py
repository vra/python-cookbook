#Univesal
def containsAny(seq, aset):
    for c in seq:
        if c in aset:
            return True
        return False


if __name__ == '__main__':
    print containsAny('abcd', 'ac')
