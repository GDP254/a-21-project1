from models.room import Room
from models.fellow import Fellow
from models.dojo import Dojo

class LivingSpace(Room):

	capacity = 6
	type_ = "LivingSpace"
	__livingspaces = dict()

	@staticmethod
	def add(cls, livingspace):
		cls.filter_livingspace(livingspace)
		Dojo.add_room(livingspace)
		cls.__livingspaces.update({livingspace.name: 
									[{capacity: livingspace.capacity}, 
										{type_: livingspace.type_}]})

	@staticmethod
	def remove(cls, livingspace):
		cls.filter_livingspace(livingspace)
		Dojo.remove_room(livingspace)
		del cls.__livingspaces[livingspace.name]

	@staticmethod
	def filter_livingspace(cls, livingspace):
		if not isinstance(livingspace, LivingSpace):
			raise TypeError("Only type living space allowed")

	"""
	# Overide Room class, only accept instances of Fellow
	def allocate_to(self, fellow):
		self.filter(fellow)
		super().allocate_to(fellow)
	"""

	"""
	def arrogate_from(self, fellow):
		self.filter(fellow)
		super().arrogate_from(fellow)
	"""

	"""
	def has_allocation(self, fellow):
		self.filter(fellow)
		super().has_allocation(fellow)
	"""
	#Only accept instances of Fellow
	def filter(self, fellow):
		if not isinstance(fellow, Fellow):
			raise TypeError("Only type Fellow allowed")