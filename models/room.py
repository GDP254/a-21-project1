from pathlib import Path

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from models.person import Person
from models.state import allocations, allocations_set, allocations_name_type, persons_detail, persons_phone

"""Narrative

Rooms are spaces within the Dojo.
They can have unique names, capacity and two types
 i.e. Office/ LivingSpace.
"""

Base = declarative_base()

class Room(Base):

	name = "Room"
	capacity = 0
	type_ = "ROOM"

	__tablename__ = "rooms"

	id_ = Column(Integer, primary_key=True)
	roomname = Column(String(25), unique=True)
	roomcapacity = Column(Integer)
	roomtype = Column(String(25))

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
		#db
		self.roomname = self.name
		self.roomtype = self.type_
		self.roomcapacity = self.roomcapacity

	@classmethod
	def save_state(cls, file_name="default"):
		path = "db/"
		file_ = file_name+".db"
		engine = create_engine("sqlite:///"+path+file_, echo=False)
		cls.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)
		session = Session()
		from models.dojo import Dojo
		rooms = cls.rooms()
		for room_name, room_detail in rooms.items():
			#Create new instance of person
			capacity = room_detail[0]["capacity"]
			type_ = room_detail[1]["type_"]
			new_room = cls(room_name)
			new_room.set_capacity(capacity)
			new_room.set_type(type_)
			session.add(new_room)
		session.commit()
		session.close()

	#setter only to used in the process of saving state
	def set_capacity(self, capacity):
		self.capacity = capacity
		self.roomcapacity = capacity

	#setter only to used in the process of saving state
	def set_type(self, type_):
		self.type_ = type_
		self.roomtype = type_

	@classmethod
	def load_state(cls, file_name="default"):
		cls.clear()
		path = "db/"
		file_ = file_name+".db"
		engine = create_engine("sqlite:///"+path+file_, echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		room_info = session.query(Room).filter_by(roomtype=cls.__name__.upper()).all()
		for room in room_info:
			room_ = cls(room.roomname)
			room_.set_capacity(room.roomcapacity)
			room_.set_type(room.roomtype)
			cls.add(room_)
		session.close()

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
	def all_allocated_rooms(cls):
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
			raise ValueError("%s-%s is already in %s-%s" % (person.phone, person.last_name, room.name, room.type_))
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

		"""Fellow or Staff allocated to Office or LivingSpace

				if person is Fellow and person has allocation to office alone:
					if destined room type is office:
						allow reallocation from office
					if destined room type is LivingSpace:
						allow allocation to LivingSpace
				if person is Fellow and person has allocation to livingspace alone:
					if destined room type is office:
						allow allocation to office
					if destined room type is LivingSpace:
						allow reallocation from LivingSpace
				if person is Staff and has allocation to office alone:
					allow reallocation from office
		"""
		"""Fellow allocated to Office and LivingSpace

				if person is Fellow and person has allocation to both office and livingspace:
					if destined room type is office:
						allow reallocation from office
					if destined room type is LivingSpace:
						allow reallocation from LivingSpace
		"""

		if len(current_allocations) > 0:
			if len(current_allocations) is 1:
				allocation = current_allocations[0]
				allocated_type = allocation[1]
				allocated_name = allocation[0]
				if person.type_ is "FELLOW":
					if allocated_type == room.type_:
						if room.type_ == "LIVINGSPACE":
							#if person is Fellow and person has allocation to livingspace alone and destined room type is LivingSpace
							from models.livingspace import LivingSpace
							old = LivingSpace.from_name(allocated_name)
							old.arrogate_from(person)
							room.allocate_to(person)
							print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))
						elif room.type_ == "OFFICE":
							#if person is Fellow and person has allocation to office alone and destined room type is office
							from models.office import Office
							old = Office.from_name(allocated_name)
							old.arrogate_from(person)
							room.allocate_to(person)
							print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))
						else:
							raise ValueError("Data in Invalid State. Room type other than LivingSpace and Office allocated.")
					else:
						#if person is Fellow and person has allocation to either livingspace or office alone and destined room type is the opposite
						if person.type_ == "STAFF":
							raise ValueError("Cannot reallocate staff to livingspace.")
						room.allocate_to(person)
						print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))
				elif person.type_ is "STAFF":
					if allocated_type == room.type_:
						if room.type_ == "OFFICE":
							#if person is Staff and has allocation to office alone
							from models.office import Office
							old = Office.from_name(allocated_name)
							old.arrogate_from(person)
							room.allocate_to(person)
							print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))
						else:
							raise ValueError("Cannot reallocate staff to livingspace.")
					else:
						raise ValueError("Staff may only be allocated to offices. Allocated room type and destined room type to dont match.")
			elif len(current_allocations) is 2:
				allocation1 = current_allocations[0]
				allocated_type1 = allocation1[1]
				allocated_name1 = allocation1[0]
				allocation2 = current_allocations[1]
				allocated_type2 = allocation2[1]
				allocated_name2 = allocation2[0]
				if person.type_ is "FELLOW":
					if allocated_type1 == room.type_:
						if room.type_ == "LIVINGSPACE":
							#if person is Fellow and person has allocation to both office and livingspace and destined room type is LivingSpace
							from models.livingspace import LivingSpace
							old = LivingSpace.from_name(allocated_name1)
							old.arrogate_from(person)
							room.allocate_to(person)
							print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))
						elif room.type_ == "OFFICE":
							#if person is Fellow and person has allocation to both office and livingspace and destined room type is office
							from models.office import Office
							old = Office.from_name(allocated_name1)
							old.arrogate_from(person)
							room.allocate_to(person)
							print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))
						else:
							raise ValueError("Data in Invalid State. Room type other than LivingSpace and Office allocated")
					elif allocated_type2 == room.type_:
						if room.type_ == "LIVINGSPACE":
							#if person is Fellow and person has allocation to both office and livingspace and destined room type is LivingSpace
							from models.livingspace import LivingSpace
							old = LivingSpace.from_name(allocated_name2)
							old.arrogate_from(person)
							room.allocate_to(person)
							print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))
						elif room.type_ == "OFFICE":
							#if person is Fellow and person has allocation to both office and livingspace and destined room type is office
							from models.office import Office
							old = Office.from_name(allocated_name2)
							old.arrogate_from(person)
							room.allocate_to(person)
							print("%s-%s reallocated to %s-%s" % (person.last_name, person.type_, room.name, room.type_))
						else:
							raise ValueError("Data in Invalid State. Room type other than LivingSpace and Office allocated")
					else:
						raise ValueError("Data in Invalid State. Allocated room type and destined room type to dont match")
				else:
					raise ValueError("Data in Invalid State. A non fellow cannot have more than one allocation")
			else:
				raise ValueError("Data in Invalid State. Person can have no more than 2 allocations")
		else:
			if room.type_ == "LIVINGSPACE":
				if person.type_ == "STAFF":
					raise ValueError("Cannot reallocate staff to livingspace.")
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
