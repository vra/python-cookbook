import time
strA = 'hello'
strB = 'world'
strC = 'python'

start_time = time.time()
print ''.join([strA, strB, strC])
print time.time() - start_time

start_time = time.time()
print strA + strB + strC
print time.time() - start_time
