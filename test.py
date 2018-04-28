from leds import LEDFactory

if __name__ == "__main__":
    ledstrip = LEDFactory.make(size=275)

    print ledstrip.size()
