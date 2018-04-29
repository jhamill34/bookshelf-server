#
# @author Joshua Rasmussen
# @description used for environments that don't have access to RpiGPIO pins
#

import sys
from LEDPlatform import LEDPlatform
from LEDColor import LEDColor
from TerminalColor import TerminalColor

class LEDStrip(LEDPlatform):
    def setup(self):
        self._strip = list()
        for i in range(self._size):
            self._strip.append(LEDColor(0, 0, 0))

    def setPixelColor(self, index, color, show=False):
        self._strip[index] = color
        if show:
            self.show()

    def batchSetPixels(self, pixels, show=False):
        pass

    def show(self):
        sys.stdout.write('\r')
        for c in self._strip:
            TerminalColor(c).display()
