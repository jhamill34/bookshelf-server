import argparse
import time
from flask import Flask, request
from flask.views import View
from leds import LEDColor, LEDFactory

def opt_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', default=10, type=int)
    return parser.parse_args()

class BaseLEDView(View):
    def __init__(self, strip):
        self.strip = strip

    def parse_color(self):
        color_json = request.get_json()
        self.color = LEDColor(color_json['red'], color_json['green'], color_json['blue'])

class SetPixelAPI(BaseLEDView):
    methods = ['POST']
    def dispatch_request(self, index):
        self.parse_color()
        self.strip.setPixelColor(index, self.color, True)

        return 'OK'

class BatchSetPixelAPI(BaseLEDView):
    methods = ['POST']
    def dispatch_request(self):
        self.parse_color()
        for i in range(self.strip.size()):
            self.strip.setPixelColor(i, self.color)
        self.strip.show()

        return 'OK'

class LEDServer:
    def __init__(self, size):
        self.app = Flask(__name__)
        self.ledstrip = LEDFactory.make(size)

    def register_views(self):
        self.app.add_url_rule('/color/<int:index>', view_func=SetPixelAPI.as_view('set_pixel', strip=self.ledstrip))
        self.app.add_url_rule('/color', view_func=BatchSetPixelAPI.as_view('batch_set_pixel', strip=self.ledstrip))

    def start(self):
        self.ledstrip.setup()
        self.ledstrip.show()
        self.app.run(host='0.0.0.0', port=3000, debug=True)

if __name__ == "__main__":
    args = opt_parse()
    s = LEDServer(size=args.num)
    s.register_views()
    s.start()
