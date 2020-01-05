import RPi.GPIO as gpio
import web

gpio.setmode(gpio.BCM)
LED = 4
ledState = False
gpio.setup(LED, gpio.OUT)


urls = (
    '/', 'index'
)


class index:
    def POST(self):
        global ledState
        if ledState == False:
            gpio.output(LED, gpio.HIGH)
            ledState = True
            return "Raspberry Pi 2 LED Pin 4 is ON"
        elif ledState == True:
            gpio.output(LED, gpio.LOW)
            ledState = False
            return "Raspberry Pi 2 LED Pin 4 is OFF"


if __name__ == '__main__':
    app = web.application (urls, globals())
    app.run()
