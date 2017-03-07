import random

from models.person import Person
from models.fellow import Fellow
from models.staff import Staff
from models.room import Room
from models.office import Office
from models.livingspace import LivingSpace
from models.dojo import Dojo
from models.state import persons_phone, persons_detail

def create_room(room_name, room_type):
	try:
		room_input_index = 0
		while room_input_index < len(room_name):
			room_type_curr = room_type[room_input_index].upper()
			room_name_curr = room_name[room_input_index].upper()
			if room_type_curr == "LIVINGSPACE":
				livingspace = LivingSpace(room_name_curr)
				LivingSpace.add(livingspace)
				print("Room (Living space): %s Added" % livingspace.name)
			elif room_type_curr == "OFFICE":
				office = Office(room_name_curr)
				Office.add(office)
				print("Room (Office): %s Added" % office.name)
			room_input_index += 1
		print(Dojo.rooms())
		print(LivingSpace.rooms())
		print(Office.rooms())
	except Exception as e:
		print(str(e))

def add_person(first_name, last_name, phone, type_, opt_in="N"):
	try:
		type_ = type_.upper()
		print(type_)
		if type_ == "FELLOW":
			fellow = Fellow(first_name, last_name, phone, opt_in)
			fellow.register()
			available_offices = Office.available() 
			if available_offices is False:
				print("There are currently no available offices")
			else:
				selection = random.choice(available_offices)
				office = Office(selection)
				office.allocate_to(fellow)
				print("Fellow: %s allocated to Office room: %s" % (fellow.name, office.name))
			if opt_in == "Y":
				available_livingspaces = LivingSpace.available()
				if available_livingspaces is False:
					print("There are currently no available living spaces")
				else:
					selection = random.choice(available_livingspaces)
					livingspace = LivingSpace(selection)
					livingspace.allocate_to(fellow)
					print("Fellow: %s allocated to Living space room: %s" % (fellow.last_name, livingspace.name))
		elif type_ == "STAFF":
			staff = Staff(first_name, last_name, phone, opt_in)
			staff.register()
			available_offices = Office.available() 
			if available_offices is False:
				print("There are currently no available offices")
			else:
				selection = random.choice(available_offices)
				office = Office(selection)
				office.allocate_to(staff)
				print("Staff: %s allocated to Office room: %s" % (fellow.last_name, office.name))
		print("Person added")
		print(persons_detail)
	except Exception as e:
		print(str(e))