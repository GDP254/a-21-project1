from models.person import Person

class Fellow(Person):

	type_ = "Fellow"
	__detail = dict()

	@staticmethod
	def register(cls, fellow):
		pass

	@staticmethod
	def has(cls, fellow):
		pass

	@staticmethod
	def all(cls):
		pass