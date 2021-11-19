from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

import usb_hid
import time

class HumanKeyboard(object):
    def __init__(self):
        self.keyboard = Keyboard(usb_hid.devices)
        self.keyboardLayout = KeyboardLayoutUS(self.keyboard)


    def keyPress(self, keyCode):
        """Send a human like keypress.

        Keyword arguments:
        keyCode -- the real key to be pressed (example Keycode.SEVEN)    
        """
        self.keyboard.press(keyCode)
        time.sleep(0.1)
        self.keyboard.release(keyCode)