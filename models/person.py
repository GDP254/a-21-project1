"""Narrative

Persons are either Staff or Fellow at the Dojo.
They can have unique phone numbers, two names and a indicator of type
 i.e. Office/ LivingSpace.
"""

class Person(object):

	first_name = None
	last_name = None
	phone = None
	type_ = "Person"
	__all_ = set([])

	def __init__(self, f_name, l_name, phone, opt_in="N"):
		self.f_name = f_name
		self.l_name = l_name
		self.phone = phone
		self.opt_in = opt_in

	@staticmethod
	def register(cls, person):
		pass

	@staticmethod
	def has(cls, person):
		pass

	@staticmethod
	def all(cls):
		pass