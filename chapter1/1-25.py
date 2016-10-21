import sys, os, htmllib, formatter

set_bold = os.popen('tput bold').read()
set_underline = os.popen('tput smu1').read()
perform_reset = os.popen('tput sgr0').read()

class TtyFormatter(formatter.AbstractFormatter):
    def __init__(self, writer):
        formatter.AbstractFormatter.__init__(self, writer)
        self.fontState = False, False
        self.fontStack = []
    def push_font(self, font):
        _, is_italic, is_bold, _ = font
        self.fontStack.append((is_italic, is_bold))
        self._updateFontState()
    def pop_font(self, *args):
        try:
            self.fontStack.pop()
        except IndexError:
            pass
        self._updateFontState()
    def _updateFontState(self):
        try:
            newState = self.fontStack[-1]
        except IndexError:
            newState = False, False
        if self.fontState != newState:
            print perform_reset
            if newState[0]:
                print set_underline
            if newState[1]:
                print set_bold
            self.fontState = newState

    myWriter = formatter.DumbWriter()
    if sys.stdout.isatty():
        myFormatter = TtyFormatter(myWriter)
    else:
        myFormatter = formatter.AbstractFormatter(myWriter)
    myParser = htmllib.HTMLParser(myFormatter)
    myParser.feed(sys.stdin.read())
    myParser.close()
