#Display unicode character on stdout
import sys,codecs
old = sys.stdout
sys.stdout = codecs.lookup('utf8')[-1](sys.stdout)
char = u'\N{LATIN SMALL LETTER A WITH DIAERESIS}'
print char
sys.stdout = old
