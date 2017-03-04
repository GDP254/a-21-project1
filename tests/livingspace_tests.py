#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

from models.livingspace import LivingSpace
from models.office import Office
from models.fellow import Fellow
from models.staff import Staff
from models.room import Room

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
		Grouping: Assign tests
		Description: The following tests confirm the assign method of the
					class Livingspace is functioning properly
	"""

	def test_allocate_to_new_optin_fellow_space(self):
		livingspace = LivingSpace('Focuspoin')
		fellow = Fellow("Neritus", "Otieno", "0784334220", "Y")
		result = livingspace.allocate_to(fellow)
		self.assertIsInstance(result, LivingSpace)

	def test_allocate_to_new_optout_fellow_space(self):
		livingspace = LivingSpace('Focuspoi')
		fellow = Fellow("Nerits", "Oteno", "0784334221", "N")
		result = livingspace.allocate_to(fellow)
		self.assertEquals(result, "Livingspace no necessary")

	def test_allocate_to_existing_fellow_space(self):
		livingspace = LivingSpace('Focuspo')
		fellow = Fellow("Nerits", "Oteno", "0784334222", "N")
		result = livingspace.allocate_to(fellow)
		self.assertEquals(result, "Fellow already has a Livingspace")

	def test_allocate_to_fellow_no_space(self):
		livingspace = LivingSpace('Focusp')
		fellow = Fellow("Neris", "Oten", "0784334223","N")
		result = livingspace.allocate_to(fellow)
		self.assertEquals(result, "Sorry the Dojo is at capacity")

	def test_allocate_to_new_staff_space(self):
		livingspace = LivingSpace('Focus')
		staff = Staff("Neritus", "Otieno", "0784334123")
		result = livingspace.allocate_to(staff)
		self.assertEquals(result, "Staff cannot be assined to a LivingSpace")

	def test_arrogate_from_existing_fellow(self):
		livingspace = LivingSpace('Focs')
		fellow = Fellow("Erits", "Teno", "0785534221", "Y")
		result_1 = livingspace.allocate_to(fellow)
		allocated_1 = livingspace.has_person(fellow)
		result_2 = livingspace.arrogate_from(fellow)
		allocated_2 = livingspace.has_person(fellow)
		self.assertEquals([allocated_1, allocated_2], [True, False])

if __name__ == '__main__':
    main()