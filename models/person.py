"""Narrative

Persons are either Staff or Fellow at the Dojo.
They can have unique phone numbers, two names and a indicator of type
 i.e. Office/ LivingSpace.
"""

class Person(object):

	first_name
	last_name
	phone
	type_
	__all_ = set([])

	def __init__(self):
		pass

	@staticmethod
	def register(cls, person):
		pass

	@staticmethod
	def has(cls, person):
		pass

	@staticmethod
	def all(cls):
		pass