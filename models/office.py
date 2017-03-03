from models.room import Room

class Office(Room):

	capacity = 4
	type_ = "Office"

	def __init__(self, name):
		self.name = name
