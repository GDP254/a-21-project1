from models.person import Person
from models.fellow import Fellow
from models.staff import Staff
from models.room import Room
from models.office import Office
from models.livingspace import LivingSpace
from models.dojo import Dojo
from models.state import persons_phone, persons_detail

def create_room(room_name, room_type):
	room_input_index = 0
	while room_input_index < len(room_name):
		room_type_curr = room_type[room_input_index].upper()
		room_name_curr = room_name[room_input_index].upper()
		room = Room(room_name_curr)
		Dojo.add_room(room)
		room_input_index += 1
	print("Room Added")
	print(Dojo.rooms())

def add_person(first_name, last_name, phone, type_, opt_in="N"):
	try:
		type_ = type_.upper()
		print(type_)
		if type_ == "FELLOW":
			fellow = Fellow(first_name, last_name, phone, opt_in)
			fellow.register()
		elif type_ == "STAFF":
			staff = Staff(first_name, last_name, phone, opt_in)
			staff.register()
		print("Person added")
		print(persons_detail)
	except Exception as e:
		print(str(e))