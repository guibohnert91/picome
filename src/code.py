import time
import board
import digitalio

from adafruit_hid.keycode import Keycode

from picome.hukeyboard import HumanKeyboard

btnLeft = digitalio.DigitalInOut(board.GP15)
btnLeft.direction = digitalio.Direction.INPUT
btnLeft.pull = digitalio.Pull.DOWN

btnCenter = digitalio.DigitalInOut(board.GP14)
btnCenter.direction = digitalio.Direction.INPUT
btnCenter.pull = digitalio.Pull.DOWN

btnRight = digitalio.DigitalInOut(board.GP13)
btnRight.direction = digitalio.Direction.INPUT
btnRight.pull = digitalio.Pull.DOWN

keyboard = HumanKeyboard()

while True:
	if btnLeft.value:
		keyboard.keyPress(Keycode.SEVEN)		

	if btnCenter.value:
		keyboard.keyPress(Keycode.EIGHT)

	if btnRight.value:
		keyboard.keyPress(Keycode.NINE)

	time.sleep(0.1)