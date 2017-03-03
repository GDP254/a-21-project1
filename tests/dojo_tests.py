from unittest import TestCase, main

from models.dojo import Dojo
from models.room import Room
from models.office import Office
from models.livingspace import LivingSpace

class TestDojo(TestCase):

	#Dojo should provide a count of current rooms
	def test_room_count(self):
		x = Dojo.room_count()
		self.assertEquals(x, len(Dojo._Dojo__rooms))

	#Dojo should be able check if a room exists
	def test_has_room(self):
		room = Office("x")
		x = Dojo.has_room(room)
		Dojo.add_room(room)
		y = Dojo.has_room(room)
		self.assertEquals([x, y], [False, True])

	#Dojo should be able to add new rooms
	def test_add_new_room(self):
		room = LivingSpace("x")
		initial_room_count = Dojo.room_count()
		initial_found_state = Dojo.has_room(room)
		Dojo.add_room(room)
		new_room_count = Dojo.room_count()
		new_found_state = Dojo.has_room(room)
		self.assertEquals([new_room_count, new_found_state],
							[initial_room_count + 1, not initial_found_state])

	#Dojo should not be able to add existing rooms
	def test_add_existing_room(self):
		room = Office("y")
		Dojo.add_room(room)
		initial_room_count = Dojo.room_count()
		initial_found_state = Dojo.has_room(room)
		with self.assertRaises(ValueError):
			Dojo.add_room(room)
		new_room_count = Dojo.room_count()
		new_found_state = Dojo.has_room(room)
		self.assertEquals([new_room_count, new_found_state],
							[initial_room_count, initial_found_state])

	#Dojo should be able to remove rooms
	def test_remove_existing_room(self):
		room = LivingSpace("x")
		initial_room_count = Dojo.room_count()
		initial_found_state = Dojo.has_room(room)
		Dojo.remove_room(room)
		new_room_count = Dojo.room_count()
		new_found_state = Dojo.has_room(room)
		self.assertEquals([new_room_count, new_found_state],
							[initial_room_count - 1, not initial_found_state])

	#Dojo name should be directly accessible
	def test_attribute_name_is_accessible(self):
		self.assertEquals(Dojo.name, "Dojo")

	#Dojo rooms should not be directly accessible
	#to allow for validation of relevant IO
	def test_rooms(self):
		self.assertTrue(isinstance(Dojo.rooms(), set))

	#Dojo should only accept rooms
	def test_filter(self):
		with self.assertRaises(TypeError):
			Dojo.filter("xy")

if __name__ == '__main__':
    main.run()