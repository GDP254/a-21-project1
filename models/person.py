from models.state import persons_detail, persons_phone

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

	def __init__(self, f_name, l_name, phone, opt_in="N"):
		input_ = [f_name, l_name, phone, opt_in]
		if "" or None in input_:
			raise ValueError("Please enter required information correctly and in full")
		f_name = str(f_name)
		l_name = str(l_name)
		names = [f_name, l_name]
		for name in names:
			if len(name) > 25:
				raise ValueError("Name too long. Please enter a shorter name")
		u = 0
		while u <= 1:
			names[u] = names[u].replace(" ", "")
			names[u] = names[u].upper()
			u += 1
		self.first_name = names[0]
		self.last_name = names[1]
		self.phone = str(phone)
		self.opt_in = opt_in

	def register(self):
		if self.registered():
			raise ValueError("Specifed phone is already registered")
		persons_phone.add(self.phone)
		persons_detail.update ({self.phone:[self.first_name, 
									self.last_name, 
									self.type_]})

	def registered(self):
		if self.phone in persons_phone:
			return True
		return False

	@staticmethod
	def all(cls):
		pass