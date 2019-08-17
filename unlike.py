from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

time.sleep(2)
n= 150
while n > 0:
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.press(Key.space)
	keyboard.release(Key.space)
	n = n - 1
	print(n)
	time.sleep(0.1)
	

