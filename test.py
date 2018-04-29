import time
import argparse
from leds import LEDFactory, LEDColor

def opt_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', default=10, type=int)
    return parser.parse_args()

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return LEDColor(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return LEDColor(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return LEDColor(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.size()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.size()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.size()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.size()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)


if __name__ == "__main__":
    args = opt_parse()

    ledstrip = LEDFactory.make(size=args.num)
    ledstrip.setup()

    colorWipe(ledstrip, LEDColor(255, 0, 0))
    rainbow(ledstrip)
    rainbowCycle(ledstrip)
