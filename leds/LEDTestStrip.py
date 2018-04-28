#
# @author Joshua Rasmussen
# @description used for environments that don't have access to RpiGPIO pins
#

from LEDPlatform import LEDPlatform
from LEDColor import LEDColor

class LEDStrip(LEDPlatform):
    def setup(self):
        self._strip = list()
        for i in range(self._size):
            self._strip[i] = LEDColor(0, 0, 0)

    def setPixelColor(self, index, color, show=False):
        print 'index: {0} - {1}'.format(index, color)

    def batchSetPixels(self, pixels, show=False):
        pass

    def show(self):
        pass
