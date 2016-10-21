def seek_op(thefilepath, record_size, record_number):
    thefile = open(thefilepath, 'rb')
    thefile.seek(record_size*record_number)
    return thefile.read(record_size)
