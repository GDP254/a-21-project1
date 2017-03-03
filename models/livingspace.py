class LivingSpace(Room):

	capacity = 6
	type_ = "LivingSpace"

	def __init__(self, name):
		pass

	# Overide Room class, only accept instances of Fellow
	def allocate_to(self, fellow):
		pass

	def arrogate_from(self, fellow):
		pass

	def has_person(self, fellow):
		pass