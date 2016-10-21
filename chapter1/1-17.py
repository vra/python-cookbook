import string
def replace_use_template(strObj):
    # New style in python2.4
    new_style = string.Template('This is $thing')
    strA = new_style.substitute(thing=2)
    print strA
    strB = new_style.substitute({'thing': 10})
    print strB

    #Old style in python2.3
    old_style = 'This is %(thing)s'
    strC = old_style % {'thing' : 'love'}
    print strC


if __name__ == '__main__':
    replace_use_template('')
