# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time

from neopixel import *
from random import randint


# LED strip configuration:
LED_COUNT      = 150   # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.


def brandonPattern(strip): #passes random values to random led
        z = randint(0,150)
        y = z-1
        for h in range(y,z):
                a = randint(0,255)
                b = randint(0,255)
                c = randint(0,255)
                strip.setPixelColor(h,Color(a,b,c))
                strip.show()
                
def colorClear(strip, color,):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()



# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	# Color wipe animations.
	#brandonPattern(strip)
	colorClear(strip, Color(0, 0, 0))  # Poweroff
	print ('Power successfully shut down to all LEDS')
		
