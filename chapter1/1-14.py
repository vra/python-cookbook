def reindent(s, numSpaces):
    leading_space = numSpaces * ' '
    lines = [leading_space + line.strip() for line in s.splitlines()]
    return '\n'.join(lines)

if __name__ == '__main__':
    print reindent('hello\nworld\nhh', 3)
