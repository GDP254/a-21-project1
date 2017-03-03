#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

class TestOffice(TestCase):

	"""
		Grouping: Attribute tests
		Description: The following tests confirm that necessary attributes exist
	"""

	def test_capacity_is_six(self):
		office = Office("Rand")
		self.assertEquals(office.capacity, 6)

	def test_has_name(self):
		office = Office("Rando")
		self.assertEquals(office.name, "Rando")

	def test_has_persons(self):
		office = Office("Rando")
		self.assertEquals(office.persons, [])

	"""
		Grouping: Constructor input tests
		Description: The following tests confirm the constructor for instances of 
					Office respond appropriately to various input
	"""

	def test_constructor_no_argument(self):
		with self.assertRaises(ValueError):
			office = Office()

	def test_constructor_empty_string(self):
		with self.assertRaises(ValueError):
			office = Office("")

	def test_constructor_none(self):
		with self.assertRaises(ValueError):
			office = Office(None)

	def test_constructor_special_characters(self):
		with self.assertRaises(ValueError):
			office = Office("@*$(£&$")

	def test_constructor_name_too_large(self):
		with self.assertRaises(ValueError):
			office = Office("Theraininspainstaysmainlyontheplainwashingawaythegrain")

	def test_constructor_spaced_name(self):
		with self.assertRaises(ValueError):
			office = Office("ri ck")

	def test_constructor_positive_integer(self):
		office = Office(23)
		self.assertEquals(office.name, "23")

	def test_constructor_positive_float(self):
		office = Office(2.3)
		self.assertEquals(office.name, "2.3")

	def test_constructor_negative_integer(self):
		office = Office(-23)
		self.assertEquals(office.name, "23")

	def test_constructor_negative_float(self):
		office = Office(-2.3)
		self.assertEquals(office.name, "2.3")

	def test_constructor_capitalize(self):
		office = Office("LOLZ")
		self.assertEquals(office.name, "Lolz")

	"""
		Grouping: Inheritance tests
		Description: The following tests confirm the instances of Office are
					sub-classes of Room
	"""

	def test_isinstance_of_room(self):
		office = Office('Focuspoint')
		self.assertIsInstance(office, Room)

	def test_notinstance_of_livingspace(self):
		office = Office('Mkuru')
		self.assertNotIsInstance(office, LivingSpace)

	"""
		Grouping: Allocate tests
		Description: The following tests confirm the assign method of the
					class Assign is functioning properly
	"""

	def test_allocate_to_new_optin_fellow_space(self):
		office = Office("No")
		fellow = Fellow("Neritus", "Otieno", "0784334220", "Y")
		result = office.allocate_to(fellow)
		self.assertIsInstance(result, Office)

	def test_allocate_to_new_optout_fellow_space(self):
		office = Office("Non")
		fellow = Fellow("Nerits", "Oteno", "0784334221", "N")
		result = office.allocate_to(fellow)
		self.assertIsInstance(result, Office)

	def test_allocate_to_existing_fellow_space(self):
		office = Office("Non4")
		fellow = Fellow("Nerits", "Oteno", "0784334222", "N")
		result = office.allocate_to(fellow)
		self.assertEquals(result, "Fellow already has an office")

	def test_allocate_to_fellow_no_space(self):
		office = Office("Nonn")
		fellow = Fellow("Neris", "Oten", "0784334223","N")
		result = office.allocate_to(fellow)
		self.assertEquals(result, "Sorry the Dojo is at capacity")

	def test_allocate_to_new_staff_space(self):
		office = Office("Nons")
		staff = Staff("Neritus", "Otieno", "0784334123")
		result = office.allocate_to(staff)
		self.assertIsInstance(result, Office)

	def test_allocate_to_existing_staff_space(self):
		office = Office("Nonx")
		staff = Staff("Nerits", "Oteno", "0784334523")
		result = office.allocate_to(staff)
		self.assertEquals(result, "Staff already has an office")

	def test_allocate_staff_no_space(self):
		office = Office("Nong")
		staff = Staff("Neris", "Oten", "0784334623")
		result = office.allocate_to(staff)
		self.assertEquals(result, "Sorry the Dojo is at capacity")

	def test_arrogate_from_existing_fellow(self):
		office = Office('Focss')
		fellow = Fellow("Erits", "Teno", "0785534221", "Y")
		result_1 = office.allocate_to(fellow)
		allocated_1 = office.has_person(fellow)
		result_2 = office.arrogate_from(fellow)
		allocated_2 = office.has_person(fellow)
		self.assertEquals([allocated_1, allocated_2], [True, False])

if __name__ == '__main__':
    main()