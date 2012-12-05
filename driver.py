# Vendor ID: 0x1D34
# Product ID: 0x0013

import usb
import alphabet
import time

class LEDMessageBoard:

	def __init__(self, vendor_id = 0x1D34, product_id = 0x0013):
		self.device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
		if self.device.is_kernel_driver_active(0) is True:
   			self.device.detach_kernel_driver(0)
		self.screen = {
			1 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			2 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			3 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			4 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			5 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			6 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			7 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		}
		self.cleared_screen = {
			1 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			2 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			3 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			4 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			5 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			6 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
			7 : [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		}

	def print_screen(self):
		for row in self.screen:
			print self.screen[row]

	def write_char(self, char, xloc, f = None):
		if f == None:
			f = alphabet.convert(char)

		fy = 1
		for y in self.screen:
			line = self.screen[y]
			for x in range(xloc, xloc + len(f[y])):
				if x >= len(self.screen[y]):
					self.screen[y].append(f[y][x - xloc])
				else:
					self.screen[y][x] = f[y][x - xloc]

		return xloc + len(f[1])

	def write_string(self, string, xloc):
		for char in string:
			xloc = self.write_char(char, xloc)

	def clear_screen(self):
		self.screen = self.cleared_screen
		self.push_screen()

	def scroll_message(self, string, xloc = 21):
		self.write_string(string, xloc)
		self.push_screen()
		for i in range(len(self.screen[1])):
			self.scroll()
			self.push_screen()
			time.sleep(0.1)



	def scroll(self):
		for row in self.screen:
			line = self.screen[row]
			for i in range(len(line)):
				if i-1 > 0:
					self.screen[row][i-1] = self.screen[row][i]
				if i+1 < len(line):
					self.screen[row][i] = self.screen[row][i+1]
				else:
					self.screen[row][i] = 1

	def push_screen(self):
		lines = []
		for row in self.screen:
			line = self.screen[row][0:21]
			# line.reverse()
			lines.append(line)

		for i in range(0, len(lines), 2):
			byte_4_range = [unicode(item) for item in lines[i][0:8]]
			byte_4_range.reverse()
			byte_3_range = [unicode(item) for item in lines[i][8:16]]
			byte_3_range.reverse()
			byte_2_range = [unicode(item) for item in lines[i][16:21]]
			byte_2_range.reverse()
			byte_4 = ''.join(byte_4_range)
			byte_3 = ''.join(byte_3_range)
			byte_2 = ''.join(byte_2_range)

			byte_4 = hex(int(byte_4, 2))
			byte_3 = hex(int(byte_3, 2))
			byte_2 = hex(int(byte_2, 2))

			if(i < 6):
				byte_7_range = [unicode(item) for item in lines[i+1][0:8]]
				byte_7_range.reverse()
				byte_6_range = [unicode(item) for item in lines[i+1][8:16]]
				byte_6_range.reverse()
				byte_5_range = [unicode(item) for item in lines[i+1][16:21]]
				byte_5_range.reverse()
				byte_7 = ''.join(byte_7_range)
				byte_6 = ''.join(byte_6_range)
				byte_5 = ''.join(byte_5_range)
			else:
				byte_7 = '11111111'
				byte_6 = '11111111'
				byte_5 = '11111111'

			byte_7 = hex(int(byte_7, 2))
			byte_6 = hex(int(byte_6, 2))
			byte_5 = hex(int(byte_5, 2))


			byte_0 = '0x00'
			byte_1 = hex(i)


			bytes = [byte_0, byte_1, byte_2, byte_3, byte_4, byte_5, byte_6, byte_7]
			bytes = [int(item, 16) for item in bytes]

			self.write(bytes)
 
	def write(self, bytes):
		return self.device.ctrl_transfer(0x21,0x09,0,0,bytes)

