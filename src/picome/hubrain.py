import time

class HumanBrain(object):
    def __init__(self):
        self.minKeyPress = 10
        self.maxKeyPress = 100

        self.timeAwareDeviation = 0.3

    def keyPress(self):
        """Send a human like keypress.

        Keyword arguments:
        keyCode -- the real key to be pressed (example Keycode.SEVEN)    
        """
        self.keyboard.press(keyCode)
        time.sleep(0.1)
        self.keyboard.release(keyCode)