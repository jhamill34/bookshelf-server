#
# @author Joshua Rasmussen
# @description Abstract class that defines the base methods to be shared
#   between various implementations of led strips
#

class LEDPlatform:
    def __init__(self, size=0):
        self._size = size

    #
    # perform any setup required to start working
    #
    def setup(self):
        pass

    #
    # Set the color of a particular pixel by using an index
    # @params index {number} the position of the pixel
    # @params color {LEDColor} the color to set the pixel
    # @params show  {bool} If set to true immediately show the pixel
    #
    def setPixelColor(self, index, color, show=False):
        pass

    #
    # Set several pixels at once by sending in an array of colors
    # where the index in the array maps to the index of the pixels
    # @params pixels {List<LEDColor>} array of pixel colors
    # @params show   {boolean} if set to true immediately show the batch
    #
    def batchSetPixels(self, pixels, show=False):
        pass

    #
    # Send signal to show whatever pixel colors have been set
    #
    def show(self):
        pass

    #
    # @returns the number of pixels
    #
    def size(self):
        return self._size
