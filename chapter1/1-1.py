import sets
def print_char(c):
    print c

map(print_char, 'abc')

string_a = sets.Set('abcd')
print(string_a)
string_b = sets.Set('defg')
print(string_b)

print string_a & string_b
