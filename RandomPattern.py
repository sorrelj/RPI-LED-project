
import time

from neopixel import *
from random import randint
import pywapi



# LED strip configuration:
LED_COUNT      = 150
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 5
LED_BRIGHTNESS = 255
LED_INVERT     = False


# Define functions


def colorClear(strip):
        for i in range(0,150):
                strip.setPixelColor(i,Color(0,0,0))
                strip.show()

def Pattern1(strip): #passes random values to random led
        z = randint(0,150)
        y = z-1
        for h in range(y,z):
                a = randint(0,255)
                b = randint(0,255)
                c = randint(0,255)
                strip.setPixelColor(h,Color(a,b,c))
                strip.show()


# Main program logic
if __name__ == '__main__':
	# Create NeoPixel object
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library
	strip.begin()



	# print ('Press Ctrl-C to quit.')
        while True:
		# Color wipe animations.
		Pattern1(strip)
		colorClear(strip)  # Poweroff
