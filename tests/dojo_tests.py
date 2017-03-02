from unittest import TestCase, main

class TestDojo(TestCase):

	#Dojo should provide a count of current rooms
	def test_room_count(self):
		x = Dojo.room_count
		self.assertEquals(x, len(Dojo._Dojo_rooms))

	#Dojo should be able check if a room exists
	def test_find_room(self):
		room = Room("x")
		x = Dojo.has_room(room)
		Dojo.add_room(room)
		y = Dojo.has_room(room)
		self.assertEquals([x, y], [False, True])

	#Dojo should be able to add rooms
	def test_add_new_room(self):
		room = Room("x")
		initial_room_count = Dojo.room_count
		initial_found_state = Dojo.has_room(room)
		Dojo.add_room(room)
		new_room_count = Dojo.room_count
		new_found_state = Dojo.find_room(room)
		self.assertEquals([new_room_count, new_found_state],
							[initial_room_count + 1, not initial_found_state])

	#Dojo should be able to remove rooms
	def test_remove_existing_room(self):
		room = Room("x")
		initial_room_count = Dojo.room_count()
		initial_found_state = Dojo.find_room("x")
		Dojo.remove_room(room)
		new_room_count = Dojo.room_count()
		new_found_state = Dojo.find_room("x")
		self.assertEquals([new_room_count, new_found_state],
							[initial_room_count - 1, not initial_found_state])

	#Dojo should not be instantiated
	def test_constructor_instantiation_not_possible(self):
		with self.assertRaises(ValueError):
			dojo = Dojo()

	#Dojo name should be directly accessible
	def test_attribute_name_is_accessible(self):
		self.assertEquals(Dojo.name, "Dojo")

	#Dojo rooms should not be directly accessible
	#to allow for validation of relevant IO
	def test_attribute_rooms_not_accessible(self):
		pass

if __name__ == '__main__':
    main.run()