"""Narrative

The Dojo is a facility that holds a set of uniquely named rooms.
It should not be instantiated and should allow for the addition and removal of rooms.
"""

class Dojo(object):

	name = 'Dojo'
	__rooms = set([])

	def __init__(self):
		pass

	@classmethod
	def room_count(cls):
		return 0

	@property
	def rooms(cls):
		pass

	@classmethod
	def add_room(cls, room):
		pass

	@classmethod
	def remove_room(cls, room):
		pass

	@classmethod
	def has_room(cls, room):
		pass