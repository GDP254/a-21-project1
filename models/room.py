from models.person import Person
from models.state import allocations, allocations_set, allocations_name_type, persons_detail, persons_phone

"""Narrative

Rooms are spaces within the Dojo.
They can have unique names, capacity and two types
 i.e. Office/ LivingSpace.
"""

class Room(object):

	name = "Room"
	capacity = 0
	type_ = "ROOM"

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
		self.type_ = self.type_.upper()

	"""
	@classmethod
	def from_name(cls, name):
		#Differed import due to cyclic import problem 
		from models.dojo import Dojo
		room = cls(name)
		if Dojo.has_room(room):
			return room
		else:
			raise ValueError("Room not found")
	"""

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
		if allocations_name_type.count(allocation_name_type_str)+1 <= self.capacity:
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

		if len(allocations) > 0:
			output = []
			for column in allocations:
				name = column[0]
				if name == self.name:
					output.append(column)
			return output
		else:
			raise Exception("%s has no persons allocated." % self.name)

	@classmethod
	def all_allocations(cls):
		"""To Do

		Retrieve all allocations
		call members function with allocation as argument
		"""

		return allocations

	@classmethod
	def all_allocated_phones(cls):
		"""To Do

		Retrieve all unique phone numbers in allocations
		"""

		output = []
		for column in allocations:
			phone = column[2]
			output.append(phone)
		output = set(output)
		return output

	@classmethod
	def all_unallocated_phones(cls):
		allocated = cls.all_allocated_phones()
		all_ = persons_phone
		unallocated = all_ - allocated
		return unallocated

	@classmethod
	def all_allocated_persons(cls):
		phones = cls.all_allocated_phones()
		output = ""
		for phone in phones:
			detail = persons_detail[phone]
			first_name = detail[0]
			last_name = detail[1]
			type_ = detail[2]
			opt_in = detail[3]
			output += "%s, %s, %s, %s\n" % (phone, last_name, first_name, type_)
		return output

	@classmethod
	def all_unallocated_persons(cls):
		"""To Do

		Retrieve all unique phone numbers in allocations
		"""

		phones = cls.all_unallocated_phones()
		output = ""
		for phone in phones:
			detail = persons_detail[phone]
			first_name = detail[0]
			last_name = detail[1]
			type_ = detail[2]
			opt_in = detail[3]
			output += "%s, %s, %s, %s\n" % (phone, last_name, first_name, type_)
		return output

	@classmethod
	def all_unallocated_rooms(cls):
		output = []
		for column in allocations:
			name = column[0]
			output.append(name)
		output = set(output)
		return output

	@classmethod
	def all_unallocated_rooms(cls):
		allocated = cls.all_allocated_rooms()
		all_ = Dojo.rooms()
		unallocated = all_ - allocated
		return unallocated

	@classmethod
	def members(cls, allocations_, room_tag=False):
		"""To Do

		For each allocation:
			Create a new instance of person
			print person information presentably
			e.g. tag (if not None), Phone, Last name, First Name, Fellow/Staff
		"""
		output = ""
		for column in allocations_:
			room_name = column[0]
			room_type = column[1]
			phone = column[2]
			detail = persons_detail[phone]
			first_name = detail[0]
			last_name = detail[1]
			type_ = detail[2]
			opt_in = detail[3]
			if room_tag is False:
				output += "%s, %s, %s, %s\n" % (phone, last_name, first_name, type_)
			else:
				output += "%s-%s, %s, %s, %s, %s\n" % (room_name, room_type, phone, last_name, first_name, type_)
		return output

	@classmethod
	def to_file(cls, content, name="File"):
		path = "output/"
		file_name = "%s.txt" % name
		f = open(path+file_name, "w")
		f.write(content)
		f.close()

	@classmethod
	def reallocate(cls, person, room):
		#Check if room user is allocating to has the allocation or is lacking capacity
		if room.has_allocation(person):
			raise ValueError("%s is already in %s" % (persons_phone+"-"+person.last_name, room.room_name+"-"+room_type))
		if room.has_capacity() is False:
			raise ValueError("Sorry %s is at capacity" % room.name)
		#Get all current allocations to the given person 
		current_allocations = []
		allocated_phones = cls.all_allocated_phones()
		if person.phone in allocated_phones:
			for allocation in allocations:
				phone = allocation[2]
				if phone == person.phone:
					current_allocations.append(allocation)
		if len(current_allocations) > 0: 
			#For each current allocation
			for allocation in current_allocations:
				type_ = allocation[1]
				name = allocation[0]
				#Allocate if the room they are coming from is of the same type
				if type_ == "LIVINGSPACE" and room.type_ == "LIVINGSPACE":
					from models.livingspace import LivingSpace
					old = LivingSpace.from_name(name)
					old.arrogate_from(person)
					room.allocate_to(person)
					print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))
					break
				elif type_ == "OFFICE" and room.type_ == "OFFICE":
					from models.office import Office
					old = Office.from_name(name)
					old.arrogate_from(person)
					room.allocate_to(person)
					print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))
					break
		else:
			if room.type_ == "LIVINGSPACE":
				room.allocate_to(person)
				print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))
			elif room.type_ == "OFFICE":
				room.allocate_to(person)
				print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))

	@classmethod
	def clear(cls):
		"""To Do

		Clear all data stores relevant to rooms for testing purposes
		"""

		del allocations[:]
		allocations_set.clear()
		del allocations_name_type[:]
