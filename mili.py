import time

import keyboard
import pynput
from pynput.keyboard import Key, Listener

class Keylogger:

    def __init__(self):
        self.count = 0
        self.keys = []

    def on_press(self, key):
        print(key, "pressed")


    def on_release(self, key):

        if key == Key.esc:
            return False
        if key == Key.f4:
            keyboard.send('4')
            keyboard.send('2')
            while True:
                time.sleep(0.10)
                keyboard.send('e')



if __name__ == "__main__":
    obj = Keylogger()
    with Listener(on_press=obj.on_press, on_release=obj.on_release) as listener:
        listener.join()