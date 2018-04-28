#
# @author Joshua Rasmussen
# @description Factory class used to abstract away the various led strip
#   implementations from the client
#

try:
    from LEDStrip import LEDStrip
except ImportError:
    from LEDTestStrip import LEDStrip

class LEDFactory:
    #
    # @params size the number of leds to use
    # @returns LEDPlatform
    #
    @staticmethod
    def make(size=0):
        return LEDStrip(size)
