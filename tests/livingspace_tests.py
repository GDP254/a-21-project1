#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

class TestLivingSpace(TestCase):

	"""
		Grouping: Attribute tests
		Description: The following tests confirm that necessary attributes exist
	"""

	def test_capacity_is_four(self):
		livingspace = LivingSpace("Rand")
		self.assertEquals(livingspace.capacity, 4)

	def test_has_name(self):
		livingspace = LivingSpace("Rando")
		self.assertEquals(livingspace.name, "Rando")

	def test_has_persons(self):
		livingspace = LivingSpace("Rando")
		self.assertEquals(livingspace.persons, [])

	"""
		Grouping: Constructor input tests
		Description: The following tests confirm the constructor for instances of 
					LivingSpace respond appropriately to various input
	"""

	def test_constructor_no_argument(self):
		with self.assertRaises(ValueError):
			livingspace = LivingSpace()

	def test_constructor_empty_string(self):
		with self.assertRaises(ValueError):
			livingspace = LivingSpace("")

	def test_constructor_none(self):
		with self.assertRaises(ValueError):
			livingspace = LivingSpace(None)

	def test_constructor_special_characters(self):
		with self.assertRaises(ValueError):
			livingspace = LivingSpace("@*$(£&$")

	def test_constructor_name_too_large(self):
		with self.assertRaises(ValueError):
			livingspace = LivingSpace("Theraininspainstaysmainlyontheplainwashingawaythegrain")

	def test_constructor_spaced_name(self):
		with self.assertRaises(ValueError):
			livingspace = LivingSpace("ri ck")

	def test_constructor_positive_integer(self):
		livingspace = LivingSpace(23)
		self.assertEquals(livingspace.name, "23")

	def test_constructor_positive_float(self):
		livingspace = LivingSpace(2.3)
		self.assertEquals(livingspace.name, "2.3")

	def test_constructor_negative_integer(self):
		livingspace = LivingSpace(-23)
		self.assertEquals(livingspace.name, "23")

	def test_constructor_negative_float(self):
		livingspace = LivingSpace(-2.3)
		self.assertEquals(livingspace.name, "2.3")

	def test_constructor_capitalize(self):
		livingspace = LivingSpace("LOLZ")
		self.assertEquals(livingspace.name, "Lolz")

	"""
		Grouping: Inheritance tests
		Description: The following tests confirm the instances of LivingSpace are
					sub-classes of Room
	"""

	def test_isinstance_of_room(self):
		livingspace = LivingSpace('Focuspoint')
		self.assertIsInstance(livingspace, Room)

	def test_notinstance_of_Office(self):
		livingspace = LivingSpace('Mkuru')
		self.assertNotIsInstance(livingspace, Office)

	"""
		Grouping: Save state tests
		Description: The following tests confirm the save_state method of the
					class Livingspace is functioning properly
	"""

	def test_save_state_room_exists_error(self):
		livingspace = LivingSpace('Nderi')
		livingspace.save_state()
		livingspace_1 = LivingSpace('Nderi')
		with self.assertRaises(ValueError):
			livingspace_1.save_state()

	def test_save_state_room_exists(self):
		livingspace = LivingSpace('Nderitu')
		initial_room_count = len(State.rooms)
		livingspace.save_state()
		livingspace_1 = LivingSpace('Nderitu')
		livingspace = LivingSpace_1.save_state()
		new_room_count = len(State.rooms)
		self.assertEquals(initial_room_count, new_room_count)

	def test_save_state_new_room(self):
		livingspace = LivingSpace("Standard")
		initial_room_count = len(State.rooms)
		livingspace.save_state()
		new_room_count = len(State.rooms)
		self.assertEquals(initial_room_count + 1, new_room_count)

	"""
		Grouping: Assign tests
		Description: The following tests confirm the assign method of the
					class Livingspace is functioning properly
	"""

	def test_assign_new_optin_fellow_space(self):
		fellow = Fellow("Neritus", "Otieno", "0784334220", "Y")
		result = livingspace.assign(fellow)
		self.assertIsInstance(result, Livingspace)

	def test_assign_new_optout_fellow_space(self):
		fellow = Fellow("Nerits", "Oteno", "0784334221", "N")
		result = LivingSpace.assign(fellow)
		self.assertEquals(result, "Livingspace no necessary")

	def test_assign_existing_fellow_space(self):
		fellow = Fellow("Nerits", "Oteno", "0784334222", "N")
		result = LivingSpace.assign(fellow)
		self.assertEquals(result, "Fellow already has a Livingspace")

	def test_assign_fellow_no_space(self):
		fellow = Fellow("Neris", "Oten", "0784334223","N")
		result = LivingSpace.assign(fellow)
		self.assertEquals(result, "Sorry the Dojo is at capacity")

	def test_assign_new_staff_space(self):
		staff = Staff("Neritus", "Otieno", "0784334123")
		result = LivingSpace.assign(staff)
		self.assertEquals(result, "Staff cannot be assined to a LivingSpace")

	def test_assign_existing_staff_space(self):
		staff = Staff("Nerits", "Oteno", "0784334523")
		result = LivingSpace.assign(staff)
		self.assertEquals(result, "Staff already has an office")

	def test_assign_staff_no_space(self):
		staff = Staff("Neris", "Oten", "0784334623")
		result = LivingSpace.assign(staff)
		self.assertEquals(result, "Sorry the Dojo is at capacity")

if __name__ == '__main__':
    main()