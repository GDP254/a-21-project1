#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

from models.livingspace import LivingSpace
from models.office import Office
from models.fellow import Fellow
from models.staff import Staff
from models.room import Room
from models.state import allocations
from models.dojo import Dojo

class TestLivingSpace(TestCase):

	def test_available_livingspace(self):
		result = LivingSpace.available()
		livingspace  = LivingSpace('MyO55e80')
		LivingSpace.add(livingspace)
		fellow = Fellow("staff"+"Njsiritus", "staff"+"Otsdeno", "0700004537", "Y")
		livingspace.allocate_to(fellow)
		fellow = Fellow("staff"+"Njsiritus", "staff"+"Otsdeno", "0700005537", "Y")
		livingspace.allocate_to(fellow)
		fellow = Fellow("staff"+"Njsiritus", "staff"+"Otsdeno", "0700006537", "Y")
		livingspace.allocate_to(fellow)
		result_2 = LivingSpace.available()
		fellow = Fellow("staff"+"Njsiritus", "staff"+"Otsdeno", "0700007537", "Y")
		livingspace.allocate_to(fellow)
		fellow = Fellow("staff"+"Njsiritus", "staff"+"Otsdeno", "0700008537", "Y")
		livingspace.allocate_to(fellow)
		fellow = Fellow("staff"+"Njsiritus", "staff"+"Otsdeno", "0700009537", "Y")
		livingspace.allocate_to(fellow)
		result_3 = LivingSpace.available()
		self.assertTrue([result, result_3, type(result_2)],
						 [False, False, "set"])

	"""
		Grouping: Attribute tests
		Description: The following tests confirm that necessary attributes exist
	"""

	def test_capacity_is_six(self):
		livingspace = LivingSpace("Rand")
		self.assertEqual(livingspace.capacity, 6)

	def test_has_name(self):
		livingspace = LivingSpace("Rando")
		self.assertEqual(livingspace.name, "RANDO")

	"""
		Grouping: Constructor input tests
		Description: The following tests confirm the constructor for instances of 
					LivingSpace respond appropriately to various input
	"""

	def test_constructor_empty_string(self):
		with self.assertRaises(ValueError):
			livingspace = LivingSpace("")

	def test_constructor_none(self):
		with self.assertRaises(ValueError):
			livingspace = LivingSpace(None)

	def test_constructor_name_too_large(self):
		with self.assertRaises(ValueError):
			livingspace = LivingSpace("Theraininspainstaysmainlyontheplainwashingawaythegrain")

	def test_constructor_spaced_name(self):
		livingspace = LivingSpace("ri ck")
		self.assertEqual(livingspace.name, "RI_CK")

	def test_constructor_positive_integer(self):
		livingspace = LivingSpace(23)
		self.assertEqual(livingspace.name, "23")

	def test_constructor_positive_float(self):
		livingspace = LivingSpace(2.3)
		self.assertEqual(livingspace.name, "2.3")

	def test_constructor_negative_integer(self):
		livingspace = LivingSpace(-23)
		self.assertEqual(livingspace.name, "23")

	def test_constructor_negative_float(self):
		livingspace = LivingSpace(-2.3)
		self.assertEqual(livingspace.name, "2.3")

	def test_constructor_capitalize(self):
		livingspace = LivingSpace("Lolz")
		self.assertEqual(livingspace.name, "LOLZ")

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
		Grouping: Allocate tests
		Description: The following tests confirm the assign method of the
					class Livingspace is functioning properly
	"""

	def test_allocate_to_new_fellow_space(self):
		livingspace = LivingSpace('Focuspoin')
		fellow = Fellow("Neritus", "Otieno", "0784334220", "Y")
		result = len(allocations)
		livingspace.allocate_to(fellow)
		result_1 = len(allocations)
		self.assertEqual(result+1, result_1)

	"""
	def test_allocate_to_new_optout_fellow_space(self):
		livingspace = LivingSpace('Focuspoi')
		fellow = Fellow("Nerits", "Oteno", "0784334221", "N")
		result = livingspace.allocate_to(fellow)
		self.assertEquals(result, "Livingspace no necessary")
	"""

	def test_allocate_to_existing_fellow_space(self):
		livingspace = LivingSpace('Focuspo')
		fellow = Fellow("Nerits", "Oteno", "0784334222", "N")
		livingspace.allocate_to(fellow)
		with self.assertRaises(ValueError):
			livingspace.allocate_to(fellow)

	def test_allocate_to_fellow_no_space(self):
		livingspace = LivingSpace('Focusp')
		with self.assertRaises(ValueError):
			x = 0
			while (x <= 7):
				suffix = str(x)
				fellow = Fellow("Neris"+suffix, "Oten"+suffix, "078433448"+suffix,"N")
				livingspace.allocate_to(fellow)
				x += 1

	def test_allocate_to_new_staff_space(self):
		livingspace = LivingSpace('Focus')
		staff = Staff("Neritus", "Otieno", "0784334123")
		with self.assertRaises(TypeError):
			result = livingspace.allocate_to(staff)

	def test_arrogate_from_existing_fellow(self):
		livingspace = LivingSpace('Focs')
		fellow = Fellow("Erits", "Teno", "0785534224", "Y")
		livingspace.allocate_to(fellow)
		allocated_1 = livingspace.has_allocation(fellow)
		livingspace.arrogate_from(fellow)
		allocated_2 = livingspace.has_allocation(fellow)
		self.assertEqual([allocated_1, allocated_2], [True, False])

	def test_add_living_space(self):
		livingspace = LivingSpace('MySpace78')
		initial_room_count = len(Dojo.rooms())
		initial_livingspace_count = len(LivingSpace.rooms())
		LivingSpace.add(livingspace)
		new_room_count = len(Dojo.rooms())
		new_livingspace_count = len(LivingSpace.rooms())
		self.assertEqual([initial_room_count+1, initial_livingspace_count+1],
						 [new_room_count, new_livingspace_count])

	def test_add_an_existing_living_space(self):
		livingspace = LivingSpace('MySpace4545')
		LivingSpace.add(livingspace)
		with self.assertRaises(ValueError):
			LivingSpace.add(livingspace)
	
	def test_remove_living_space(self):
		livingspace = LivingSpace('MySpace89')
		LivingSpace.add(livingspace)
		initial_room_count = len(Dojo.rooms())
		initial_livingspace_count = len(LivingSpace.rooms())
		print(LivingSpace.rooms())
		LivingSpace.remove(livingspace)
		new_room_count = len(Dojo.rooms())
		new_livingspace_count = len(LivingSpace.rooms())
		print(LivingSpace.rooms())
		self.assertEqual([initial_room_count-1, initial_livingspace_count-1],
						 [new_room_count, new_livingspace_count])

if __name__ == '__main__':
    main()