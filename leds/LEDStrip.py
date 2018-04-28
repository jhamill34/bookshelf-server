#
# @author Joshua Rasmussen
# @description Uses the neopixel library and is the main class that is to be
#   used on actual hardware
#

from neopixel import *
from LEDPlatform import LEDPlatform

# LED strip configuration:
LED_COUNT      = 275     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

class LEDStrip(LEDPlatform):
    def setup(self):
        self._strip = Adafruit_NeoPixel(self._size, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        self._strip.begin()

    def _convertColor(self, c):
        return Color(c.red, c.green, c.blue)

    def setPixelColor(self, index, color, show=False):
        self._strip.setPixelColor(index, self._convertColor(color))
        if show:
            self.show()

    def batchSetPixels(self, pixels, show=False):
        pass

    def show(self):
        self._strip.show()

    def size(self):
        return self._strip.numPixels()
