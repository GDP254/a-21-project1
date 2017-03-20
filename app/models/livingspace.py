from app.models.room import Room
from app.models.fellow import Fellow
from app.models.dojo import Dojo
from app.models.state import allocations_name_type

class LivingSpace(Room):

	capacity = 6
	type_ = "LIVINGSPACE"
	__livingspaces = dict()
	__livingspaces_set = set()

	@classmethod
	def from_name(cls, name):
		room = cls(name)
		if Dojo.has_room(room):
			room_name_type = room.name+"-"+room.type_
			if room_name_type in cls.__livingspaces_set:
				return room
			else:
				raise ValueError("Room not found")
		else:
			raise ValueError("Room not found")

	@classmethod
	def add(cls, livingspace):
		cls.filter_livingspace(livingspace)
		Dojo.add_room(livingspace)
		cls.__livingspaces_set.add("%s-%s" % (livingspace.name, livingspace.type_))
		cls.__livingspaces.update({livingspace.name: 
									[{"capacity": livingspace.capacity}, 
										{"type_": livingspace.type_}]})

	@classmethod
	def remove(cls, livingspace):
		cls.filter_livingspace(livingspace)
		Dojo.remove_room(livingspace)
		del cls.__livingspaces[livingspace.name]
		cls.__livingspaces_set.remove("%s-%s" % (livingspace.name, livingspace.type_))

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

	@classmethod
	def available(cls):
		available = set()
		if len(cls.__livingspaces_set) == 0:
			return False
		for office in cls.__livingspaces_set:
			name = office.split("-")[0]
			if office in allocations_name_type:
				if allocations_name_type.count(office) < cls.capacity:
					available.add(name)
			else:
				available.add(name)
		if len(available) == 0:
			return False
		return available