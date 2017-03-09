from models.person import Person
from models.state import allocations, allocations_set, allocations_name_type
"""Narrative

Rooms are spaces within the Dojo.
They can have unique names, capacity and two types
 i.e. Office/ LivingSpace.
"""

class Room(object):

	name = "Room"
	capacity = 0
	type_ = "Room"

	def __init__(self, name):
		if isinstance(name, float) or isinstance(name, int):
			name = abs(name)
			name = str(name)
		wrong = ["", None]
		if name in wrong:
			raise ValueError("Please enter a name for the room")
		name = name.strip()
		if len(name) > 25:
			raise ValueError("Name too long. Please enter a shorter name")
		name = name.replace(" ", "_")
		name = name.upper()
		self.name = name

	def allocate_to(self, person):
		self.filter(person)
		if self.has_allocation(person):
			raise ValueError("%s has already been allocated to room" % person.phone)
		if self.has_capacity() is False:
			raise ValueError("Sorry %s is at capacity" % self.name)
		allocation = [self.name, self.type_, person.phone]
		allocation_str = "%s-%s-%s" % (self.name, self.type_, person.phone)
		allocation_name_type_str = "%s-%s" % (self.name, self.type_)
		allocations.append(allocation)
		allocations_name_type.append(allocation_name_type_str)
		allocations_set.add(allocation_str)

	def arrogate_from(self, person):
		self.filter(person)
		if self.has_allocation(person) is False:
			raise ValueError("%s is not allocated to specified room" % person.phone)
		if self.has_capacity() is False:
			raise ValueError("Sorry %s is at capacity" % self.name)
		allocation = [self.name, self.type_, person.phone]
		allocation_str = "%s-%s-%s" % (self.name, self.type_, person.phone)
		allocation_name_type_str = "%s-%s" % (self.name, self.type_)
		allocations.remove(allocation)
		allocations_name_type.remove(allocation_name_type_str)
		allocations_set.remove(allocation_str)

	def has_allocation(self, person):
		self.filter(person)
		allocation_str = "%s-%s-%s" % (self.name, self.type_, person.phone)
		if allocation_str in allocations_set:
			return True
		return False

	def has_capacity(self):
		allocation_name_type_str = "%s-%s" % (self.name, self.type_)
		if allocations_name_type.count(allocation_name_type_str) <= self.capacity:
			return True
		return False

	def filter(self, person):
		if not isinstance(person, Person):
			raise TypeError("Only type Person allowed")

	def allocations(self):
		"""To Do

		Ensure the current instance exists

		Retrieve allocations whose first value matches 
		the name of the current instance
		"""
		pass

	@classmethod
	def all_allocations(cls):
		"""To Do

		Retrieve all allocations
		call members function with allcoation as argument
		"""
		pass

	@classmethod
	def all_unallocated(cls):
		"""To Do

		compare set of allocated to complete set of persons
		set of those who are not in the set of allocated persons
		"""
		pass

	@classmethod
	def members(cls, allocations, tag=None):
		"""To Do

		For each allocation:
			Create a new instance of person
			print person information presentably
			e.g. tag (if not None), Phone, Last name, First Name, Fellow/Staff
		"""
		pass

	@classmethod
	def clear(cls):
		"""To Do

		Clear all data stores relevant to rooms for testing purposes
		"""
		pass
