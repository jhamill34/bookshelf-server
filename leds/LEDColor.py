#
# @author Joshua Rasmussen
# @description A class used to describe an RGB color
#

import sys

class InvalidColorException(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message
    def __str__(self):
        return '{0} - {1}'.format(str(self.value), self.message)

def rgb(r, g, b):
    return "{0};{1};{2}".format(str(r), str(g), str(b))

def set_color(fg=None, bg=None):
    """
    Print escape codes to set the terminal color.
    fg and bg are indices into the color palette for the foreground and
    background colors.
    """
    if fg:
        sys.stdout.write('\x1b[38;2;%sm' % fg)
    if bg:
        sys.stdout.write('\x1b[48;2;%sm' % bg)

def reset_color():
    """
    Reset terminal color to default.
    """
    sys.stdout.write('\x1b[0m')

def print_color(str, fg=None, bg=None):
    """
    Print function, with extra arguments fg and bg to set colors.
    """
    set_color(fg, bg)
    sys.stdout.write(str)
    reset_color()
    sys.stdout.write(' ')
    sys.stdout.flush()

class LEDColor:
    def __init__(self, red, green, blue):
        self.red = self._checkValidColor(red)
        self.green = self._checkValidColor(green)
        self.blue = self._checkValidColor(blue)

    def _checkValidColor(self, c):
        if (c >= 0) and (c <= 255):
            return c
        else:
            raise InvalidColorException(c, 'Invalid color value!')

    def display(self):
        print_color('   ', bg=rgb(self.red, self.green, self.blue))
