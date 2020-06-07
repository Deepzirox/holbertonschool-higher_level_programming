#!/usr/bin/python3
Base = __import__('base').Base


class Rectangle(Base):
	def __init__(self, width, height, x=0, y=0, id=None):
		super().__init__(id)
		if type(width) not in [int]:
			raise TypeError("width must be an integer")
		elif width <= 0:
			raise ValueError("width must be > 0")
		self.__width = width
		if type(height) not in [int]:
			raise TypeError("height must be an integer")
		elif height <= 0:
			raise ValueError("height must be > 0")
		self.__height = height
		if type(x) not in [int]:
			raise TypeError("x must be an integer")
		elif x < 0:
			raise ValueError("x must be >= 0")
		self.__x = x
		if type(y) not in [int]:
			raise TypeError("y must be an integer")
		elif y < 0:
			raise ValueError("y must be >= 0")
		self.__y = y

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, width):
		if type(width) not in [int]:
			raise TypeError("width must be an integer")
		elif width <= 0:
			raise ValueError("width must be > 0")
		self.__width = width

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, height):
		if type(height) not in [int]:
			raise TypeError("height must be an integer")
		elif height <= 0:
			raise ValueError("height must be > 0")
		self.__height = height

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, x):
		if type(x) not in [int]:
			raise TypeError("x must be an integer")
		elif x < 0:
			raise ValueError("x must be >= 0")
		self.__x = x
	
	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, y):
		if type(y) not in [int]:
			raise TypeError("y must be an integer")
		elif y < 0:
			raise ValueError("y must be >= 0")
		self.__y = y

	def area(self):
		return self.__width * self.__height




if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())
