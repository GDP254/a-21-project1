from models.room import Room
"""Narrative

The Dojo is a facility that holds a set of uniquely named rooms.
It should not be instantiated and should allow for the addition and removal of rooms.
"""

class Dojo(object):

	name = 'Dojo'
	__rooms = set()

	@classmethod
	def room_count(cls):
		return len(cls.__rooms)

	@classmethod
	def rooms(cls):
		return cls.__rooms

	@classmethod
	def add_room(cls, room):
		cls.filter(room)
		if cls.has_room(room):
			raise ValueError("%s already exists." % room.name)
		cls.__rooms.add(room.name)

	@classmethod
	def remove_room(cls, room):
		cls.filter(room)
		if cls.has_room(room):
			cls.__rooms.remove(room.name)

	@classmethod
	def has_room(cls, room):
		cls.filter(room)
		if room.name in cls.__rooms:
			return True
		return False

	@classmethod
	def filter(cls, room):
		if not isinstance(room, Room):
			raise TypeError("The Dojo only contains rooms")

	@classmethod
	def clear(cls):
		"""To Do

		Clear all rooms in dojo for testing purposes
		"""

		cls.__rooms.clear()