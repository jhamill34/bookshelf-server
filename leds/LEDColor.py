#
# @author Joshua Rasmussen
# @description A class used to describe an RGB color
#

class InvalidColorException(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message
    def __str__(self):
        return '{0} - {1}'.format(str(self.value), self.message)

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

    def __str__(self):
        return 'rgb({0}, {1}, {2})'.format(self.red, self.green, self.blue)
