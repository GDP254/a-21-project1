import random
import os

from models.person import Person
from models.fellow import Fellow
from models.staff import Staff
from models.room import Room
from models.office import Office
from models.livingspace import LivingSpace
from models.dojo import Dojo
from models.allocation import Allocation
from models.state import persons_phone, persons_detail

def save_state(file_name="default"):
	file_name = str(file_name)
	path = "db/"
	file_ = file_name+".db"
	if os.path.isfile(path+file_):
		os.remove(path+file_)
	Person.save_state(file_name)
	LivingSpace.save_state(file_name)
	Office.save_state(file_name)
	Allocation.save_state(file_name)
	print_pretty("The current state of the application has successfully been saved in the db directory under the file: %s." % file_)

def load_state(file_name="default"):
	file_name = str(file_name)
	path = "db/"
	file_ = file_name+".db"
	if os.path.isfile(path+file_):
		Person.load_state(file_name)
		LivingSpace.load_state(file_name)
		Office.load_state(file_name)
		Allocation.load_state(file_name)
		print_pretty("The current state of the application has successfully been loaded from the file: %s under the directory db." % file_)
	else:
		raise Exception("Specified file does not exist")

def reallocate_person(phone, room_name):
	try:
		person = get_person(phone)
		room = get_room(room_name)
		print_pretty(Room.reallocate(person, room))
	except Exception as e:
		print_pretty(str(e))

def get_person(phone):
	try:
		return Fellow.from_phone(phone)
	except ValueError:
		pass
	try:
		return Staff.from_phone(phone)
	except ValueError:
		raise ValueError("specifed phone is unknown")

def get_room(room_name):
	try:
		return LivingSpace.from_name(room_name)
	except ValueError:
		pass
	try:
		return Office.from_name(room_name)
	except ValueError:
		raise ValueError("specifed room is unknown")

def load_people(file_name):
		try:
			path = "input/"
			file_ = path+file_name+".txt"
			file_size = os.stat(file_).st_size
			if file_size <= 0:
				raise IOError("Specified file is empty")
			with open(file_, "r") as f:
				for line in f:
					index = line.split()
					first_name = index[0]
					last_name = index[1]
					phone = index[2]
					type_ = index[3]
					opt_in = "N"
					try:
						opt_in = index[4]
					except IndexError:
						pass
					add_person(first_name, last_name, phone, type_, opt_in)
		except FileNotFoundError as e:
			print_pretty(str(e))
		except IOError as e:
			print_pretty(str(e))

def print_unallocated(out, file_name):
	output = Room.all_unallocated_persons()
	if len(output) > 0:
		if out is True:
			if file_name is not None:
				Room.to_file(output, file_name)
				print_pretty(" A list of unallocated persons can be found in the output directory under the file %s.txt" % file_name)
			else:
				Room.to_file(output)
				print_pretty(" A list of unallocated persons can be found in the output directory under the file File.txt")
		else:
			print_pretty(output)
	else:
		print_pretty("There are no unallocated persons to show")

def print_allocations(out, file_name):
	allocations = Room.all_allocations()
	output = Room.members(allocations, room_tag=True)
	if len(output) > 0:
		if out is True:
			if file_name is not None:
				Room.to_file(output, file_name)
				print_pretty(" A list of allocated persons can be found in the output directory under the file %s.txt" % file_name)
			else:
				Room.to_file(output)
				print_pretty(" A list of allocated persons can be found in the output directory under the file File.txt")
		else:
			print_pretty(output)
	else:
		print_pretty(" There are no allocations to show")

def print_room(room_name):
	try:
		room = Room(room_name)
		allocations = room.allocations()
		print_pretty(" Allocations to room: "+room.name)
		print_pretty(Room.members(allocations))
	except Exception as e:
		print_pretty(str(e))

def create_room(room_name, room_type):
	try:
		room_input_index = 0
		while room_input_index < len(room_name):
			room_type_curr = room_type[room_input_index].upper()
			room_name_curr = room_name[room_input_index].upper()
			if room_type_curr == "LIVINGSPACE":
				livingspace = LivingSpace(room_name_curr)
				LivingSpace.add(livingspace)
				print_pretty(" A living space called %s has been successfully created." % livingspace.name)
			elif room_type_curr == "OFFICE":
				office = Office(room_name_curr)
				Office.add(office)
				print_pretty(" An office called %s has been successfully created." % office.name)
			else:
				print_pretty(" The specified room type %s, is currently not supported." % room_type_curr)
			room_input_index += 1
	except Exception as e:
		print_pretty(str(e))

def add_person(first_name, last_name, phone, type_, opt_in="N"):
	try:
		type_ = type_.upper()
		if type_ == "FELLOW":
			fellow = Fellow(first_name, last_name, phone, opt_in)
			fellow.register()
			first_name = fellow.first_name
			last_name = fellow.last_name
			type_ = fellow.type_
			available_offices = Office.available() 
			if available_offices is False:
				print_pretty(" There are currently no available offices.")
			else:
				selection = random.choice(list(available_offices))
				office = Office(selection)
				office.allocate_to(fellow)
				print_pretty(" The fellow: %s has been allocated to the office: %s." % (fellow.last_name, office.name))
			if fellow.opt_in == "Y":
				available_livingspaces = LivingSpace.available()
				if available_livingspaces is False:
					print_pretty(" There are currently no available living spaces.")
				else:
					selection = random.choice(list(available_livingspaces))
					livingspace = LivingSpace(selection)
					livingspace.allocate_to(fellow)
					print_pretty(" The fellow: %s has been allocated to the living space: %s." % (fellow.last_name, livingspace.name))
		elif type_ == "STAFF":
			staff = Staff(first_name, last_name, phone, opt_in)
			staff.register()
			first_name = staff.first_name
			last_name = staff.last_name
			type_ = staff.type_
			available_offices = Office.available() 
			if available_offices is False:
				print_pretty(" There are currently no available offices.")
			else:
				selection = random.choice(list(available_offices))
				office = Office(selection)
				office.allocate_to(staff)
				print_pretty(" The staff: %s has been allocated to the office: %s." % (staff.last_name, office.name))
		else:
			print_pretty(" %s is currently not a supported role." % type_)
		print_pretty(" A %s: %s %s has been successfully created." % (type_, first_name, last_name))
		#print(persons_detail)
	except Exception as e:
		print_pretty(str(e))

def print_pretty(message):
	print("-"*70)
	print("")
	print(message)
	print("")
	print("-"*70)
