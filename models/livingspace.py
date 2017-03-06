from models.room import Room
from models.fellow import Fellow
from models.dojo import Dojo

class LivingSpace(Room):

	capacity = 6
	type_ = "LivingSpace"
	__livingspaces = dict()

	@classmethod
	def add(cls, livingspace):
		cls.filter_livingspace(livingspace)
		Dojo.add_room(livingspace)
		cls.__livingspaces.update({livingspace.name: 
									[{capacity: livingspace.capacity}, 
										{type_: livingspace.type_}]})

	@classmethod
	def remove(cls, livingspace):
		cls.filter_livingspace(livingspace)
		Dojo.remove_room(livingspace)
		del cls.__livingspaces[livingspace.name]

	@classmethod
	def rooms(cls):
		return cls.__livingspaces

	@classmethod
	def filter_livingspace(cls, livingspace):
		if not isinstance(livingspace, LivingSpace):
			raise TypeError("Only type living space allowed")

	#Only accept instances of Fellow
	def filter(self, fellow):
		if not isinstance(fellow, Fellow):
			raise TypeError("Only type Fellow allowed")