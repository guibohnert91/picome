import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

btnLeft = digitalio.DigitalInOut(board.GP15)
btnLeft.direction = digitalio.Direction.INPUT
btnLeft.pull = digitalio.Pull.DOWN

btnCenter = digitalio.DigitalInOut(board.GP14)
btnCenter.direction = digitalio.Direction.INPUT
btnCenter.pull = digitalio.Pull.DOWN

btnRight = digitalio.DigitalInOut(board.GP13)
btnRight.direction = digitalio.Direction.INPUT
btnRight.pull = digitalio.Pull.DOWN

while True:
	if btnLeft.value:
		keyboard.press(Keycode.SEVEN)
		time.sleep(0.1)
		keyboard.release(Keycode.SEVEN)
		# this code should be replaced after for a 'keypress event handler?'

	if btnCenter.value:
		keyboard.press(Keycode.EIGHT)
		time.sleep(0.1)
		keyboard.release(Keycode.EIGHT)

	if btnRight.value:
		keyboard.press(Keycode.NINE)
		time.sleep(0.1)
		keyboard.release(Keycode.NINE)

	time.sleep(0.1)