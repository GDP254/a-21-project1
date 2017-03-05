from models.person import Person

class Staff(Person):

	type_ = "Staff"
	__detail = dict()

	@staticmethod
	def register(cls, staff):
		pass

	@staticmethod
	def has(cls, staff):
		pass

	@staticmethod
	def all(cls):
		pass