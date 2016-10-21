import struct
def fields(baseformat, theline, lastfield=False):
    #baseformat = "3s 2x 5s 2x" #s:char,x:ingore
    struct.uppack(baseformat, theline)
    
