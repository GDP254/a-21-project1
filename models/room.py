"""Narrative

Rooms are spaces within the Dojo.
They can have unique names, capacity and two types
 i.e. Office/ LivingSpace.
"""

class Room(object):

	name = None
	capacity = None
	type_ = None
	allocated = set([])
	not_allocated = set([])
	persons = set([])

	def __init__(self):
		pass

	@property
	def available_room_count(self):
		pass

	@property
	def not_available_room_count(self):
		pass

	def allocate_to(self, person):
		pass

	def arrogate_from(self, person):
		pass

	def has_person(self, person):
		pass