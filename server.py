import argparse
import time
from flask import Flask, request, render_template
from flask.views import View
from leds import LEDColor, LEDFactory

LED_COUNT = 275
DEBUG = True
PORT = 3000

app = Flask(__name__)
ledstrip = LEDFactory.make(LED_COUNT)
ledstrip.setup()
ledstrip.show()

@app.route('/color/<int:index>', methods=['POST'])
def setPixelAPI(index):
    color_json = request.get_json()
    color = LEDColor(color_json['red'], color_json['green'], color_json['blue'])
    ledstrip.setPixelColor(index, color, True)

    return 'OK'

@app.route('/color', methods=['POST'])
def batchSetPixelAPI():
    color_json = request.get_json()
    color = LEDColor(color_json['red'], color_json['green'], color_json['blue'])

    for i in range(ledstrip.size()):
        ledstrip.setPixelColor(i, color)

    ledstrip.show()

    return 'OK'

@app.route('/')
def render_home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
