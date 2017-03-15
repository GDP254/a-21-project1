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

	def __init__(self, first_name, last_name, phone, opt_in="N"):
		phone = phone.replace(" ", "")
		if phone.isdigit() is False:
			raise ValueError("The phone number provided %s is invalid" % phone)
		input_ = [first_name, last_name, phone]
		if "" or None in input_:
			raise ValueError("Please enter required information correctly and in full")
		first_name = str(first_name)
		last_name = str(last_name)
		names = [first_name, last_name]
		for name in names:
			if len(name) > 25:
				raise ValueError("Name too long. Please enter a shorter name")
		name_index = 0
		while name_index <= 1:
			names[name_index] = names[name_index].replace(" ", "")
			names[name_index] = names[name_index].upper()
			name_index += 1
		if opt_in is not None:
			opt_in = opt_in.upper()
		self.first_name = names[0]
		self.last_name = names[1]
		self.phone = str(phone)
		self.opt_in = opt_in

	#alternate constructor
	@staticmethod
	def from_phone(cls, phone):
		"""To Do

		Retrieve detail recor of phone and initialize based on the information
		"""
		
		if phone in persons_phone:
			info = persons_detail[phone]
			first_name = info[0]
			last_name = info[1]
			type_ = info[2]
			opt_in = info[3]
			person = cls(first_name, last_name, phone, opt_in)
			person.type_ = type_
			return person
		else:
			raise ValueError("Specified phone does not exist")

	def register(self):
		if self.registered():
			raise ValueError("Specifed phone is already registered")
		persons_phone.add(self.phone)
		persons_detail.update ({self.phone:[self.first_name, 
									self.last_name, 
									self.type_,
									self.opt_in]})

	def registered(self):
		if self.phone in persons_phone:
			return True
		return False

	@classmethod
	def clear(cls):
		"""To Do

		Clear all data stores relevant to persons for testing purposes
		"""

		persons_detail.clear()
		persons_phone.clear()