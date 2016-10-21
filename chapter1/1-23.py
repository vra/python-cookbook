import codecs
from htmlentitydefs import codepoint2name

def encode_for_xml(unicode_data, encoding='ascii'):
    return unicode_data.encode(encoding, 'xmlcharrefreplace')

def html_replace(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeTranslateError)):
        s = [u'&%s;' % codepoint2name[ord(c)] for c in exc.object[exc.start:exc.end]]
        return ''.join(s), exc.end
    else:
        raise TypeError("can't handle %s" % exc.__name__)

    codecs.register_error('html_replace', html_replace)
def encdoe_for_html(unicode_data, encoding='ascii'):
    return unicode_data.encode(encoding, 'html_replace')

if __name__ == '__main__':
    data = u'''\
    <html>
    <body>
    <ul>
    <li>\xe0
    <li>\xe7
    <li>\xe9
    </ul>
    </body>
    </html>
    '''
    print encode_for_xml(data)
    print encdoe_for_html(data)

    # Example 2
    outfile = codecs.open('open.html', mode='w', encoding='ascii', errors='html_replace')
    outfile.write(data)
    outfile.close()
