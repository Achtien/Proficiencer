spc = ' '
dot0 = '\u25A0'	# ■
dot1 = '\u25A1'	# □ 

class Pixel(object):
	def __init__(self, name, size):
		if type(name).__name__ != 'str':
			raise TypeError("Expecting str, got {type(name)}")
		if type(size).__name__ != 'tuple':
			raise TypeError("Expecting tuple, got {type(size)}")
		if len(size) != 2:
			raise ValueError("Size not 2")

		self.size = size
		self.__name__ = name
		self.map = []
		for i in range(0, size[0]):
			line = []
			for j in range(0, size[1]):
				line.append(spc)

			self.map.append(line)

	def draw(self, dots):
		if type(dots).__name__ != 'list':
			raise TypeError("Expecting list, got {type(dots)}")
		if len(dots) != self.size[0]:
			raise ValueError("Size do not match!")
		for line in dots:
			if len(line) != self.size[1]:
				raise ValueError("Size do not match!")

		for i in range(self.size[0]):
			for j in range(self.size[1]):
				if dots[i][j]:
					self.map[i][j] = dot0

	
	def print(self):
		for i in self.map:
			line_print = ''
			for j in i:
				line_print += j
			print(line_print)


correct_pixel = Pixel('correct !!', (8, 66))
correct_pixel.draw([
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
[0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,0],
[0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
[0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0],
[0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0]
])

correct_pixel.print()
