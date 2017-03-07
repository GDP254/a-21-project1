from models.room import Room
from models.staff import Staff
from models.dojo import Dojo

class Office(Room):

	capacity = 4
	type_ = "Office"
	__offices = dict()

	@classmethod
	def add(cls, office):
		cls.filter_office(office)
		Dojo.add_room(office)
		cls.__offices.update({office.name: 
									[{"capacity": office.capacity}, 
										{"type_": office.type_}]})

	@classmethod
	def remove(cls, office):
		cls.filter_office(office)
		Dojo.remove_room(office)
		del cls.__offices[office.name]

	@classmethod
	def rooms(cls):
		return cls.__offices

	@classmethod
	def filter_office(cls, office):
		if not isinstance(office, Office):
			raise TypeError("Only type office allowed")

