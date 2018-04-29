#
# @author Joshua Rasmussen
# @description helper methods to print color to the terminal
#

import sys

class TerminalColor:
    def __init__(self, color):
        self.color = color

    #
    # Helper methods to help print to terminal using terminal codes
    #
    def _rgb(self):
        r = str(self.color.red)
        g = str(self.color.green)
        b = str(self.color.blue)
        return "{0};{1};{2}".format(r, g, b)

    def _set_color(self, fg=None, bg=None):
        if fg:
            sys.stdout.write('\x1b[38;2;%sm' % fg)
        if bg:
            sys.stdout.write('\x1b[48;2;%sm' % bg)

    def _reset_color(self):
        sys.stdout.write('\x1b[0m')

    def _print_color(self, str, fg=None, bg=None):
        self._set_color(fg, bg)
        sys.stdout.write(str)
        self._reset_color()
        sys.stdout.write(' ')
        sys.stdout.flush()

    #
    # Prints the color to the terminal using terminal color codes
    #
    def display(self):
        self._print_color('   ', bg=self._rgb())
