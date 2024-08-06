class Demo:
	def __init__(self):
		pass

	def getString(self):
		str_input = input("Please enter a string : ")
		return str_input

	def printString(self, str_input):
		name = getString()
		print(name.upper())

obj = Demo()
obj.getString()
obj.printString()