import struct
def replace_bin_file(thefilepath, record_number=0):
    format_string = "81" # in a record, there are 8 int(4 byte)
    thefile = open(thefilepath)
    record_size = struct.calcsize(format_string)
    thefile.seek(record_size*record_number)
    buffer = thefile.read(record_size)
    fields = list(struct.unpack(format_string, buffer))
    # DO the replace here!
    do_somthing_with(field)
    buffer = struct.pack(format_string, *fields)
    thefile.seek(record_size*record_number)
    thefile.write(buffer)
    thefile.close()
