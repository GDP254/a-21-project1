from models.room import Room
from models.staff import Staff
from models.dojo import Dojo
from models.state import allocations_name_type

class Office(Room):

	capacity = 4
	type_ = "Office"
	__offices = dict()
	__offices_set = set()

	@classmethod
	def add(cls, office):
		cls.filter_office(office)
		Dojo.add_room(office)
		cls.__offices_set.add("%s-%s" % (office.name, office.type_))
		cls.__offices.update({office.name: 
									[{"capacity": office.capacity}, 
										{"type_": office.type_}]})

	@classmethod
	def remove(cls, office):
		cls.filter_office(office)
		Dojo.remove_room(office)
		del cls.__offices[office.name]
		cls.__offices_set.remove("%s-%s" % (office.name, office.type_))

	@classmethod
	def rooms(cls):
		return cls.__offices

	@classmethod
	def filter_office(cls, office):
		if not isinstance(office, Office):
			raise TypeError("Only type office allowed")

	@classmethod
	def available(cls):
		available = set()
		if len(cls.__offices_set) == 0:
			return False
		for office in cls.__offices_set:
			name = office.split("-")[0]
			if office in allocations_name_type:
				if allocations_name_type.count(office) < cls.capacity:
					available.add(name)
			else:
				available.add(name)
		if len(available) == 0:
			return False
		return available

