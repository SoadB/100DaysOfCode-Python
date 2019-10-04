
class Library:
	def __init__(self, book, shelf):
		self.booknum = book
		self.bookshelf = shelf


obj = Library(300, 45)
print(obj.booknum)
print(obj.bookshelf)
print("-------------------------")


class ScienceSection(Library):
	def __init__(self, book, shelf):
		super().__init__(book, shelf)
		self.name = 'Physics books'

	def printcontent(self):
		print(self.booknum, self.bookshelf, self.name)


x = ScienceSection(300, 45)
x.printcontent()
print("-------------------------")
x = ScienceSection(20, 4)
x.printcontent()
