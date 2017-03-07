#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

from models.office import Office
from models.livingspace import LivingSpace
from models.person import Person
from models.fellow import Fellow
from models.staff import Staff
from models.room import Room
from models.state import allocations
from models.dojo import Dojo

class TestOffice(TestCase):

	def test_available_office(self):
		result = Office.available()
		office = Office('MyO55e89')
		Office.add(office)
		staff = Staff("staff"+"Njsiritus", "staff"+"Otsdeno", "0700000537", "Y")
		office.allocate_to(staff)
		staff = Staff("staff"+"Njsiritus", "staff"+"Otsdeno", "0700001537", "Y")
		office.allocate_to(staff)
		result_2 = Office.available()
		staff = Staff("staff"+"Njsiritus", "staff"+"Otsdeno", "0700002537", "Y")
		office.allocate_to(staff)
		staff = Staff("staff"+"Njsiritus", "staff"+"Otsdeno", "0700003537", "Y")
		office.allocate_to(staff)
		result_3 = Office.available()
		self.assertTrue([result, result_3, type(result_2)],
						 [False, False, "set"])

	"""
		Grouping: Inheritance tests
		Description: The following tests confirm the instances of Office are
					sub-classes of Room
	"""

	def test_isinstance_of_room(self):
		office = Office("staff"+'Focuspoint')
		self.assertIsInstance(office, Room)

	def test_notinstance_of_LivingSpace(self):
		office = Office("staff"+'Mkuru')
		self.assertNotIsInstance(office, LivingSpace)

	"""
		Grouping: Allocate tests
		Description: The following tests confirm the assign method of the
					class Office is functioning properly
	"""

	def test_allocate_to_new_staff_space(self):
		office = Office("staff"+"Foin")
		staff = Staff("staff"+"Neritus", "staff"+"Otieno", "0784334537", "Y")
		result = len(allocations)
		office.allocate_to(staff)
		result_1 = len(allocations)
		self.assertEqual(result+1, result_1)

	def test_allocate_to_new_fellow_space(self):
		office = Office("staff"+"Foin")
		fellow = Fellow("staff"+"Neritus", "staff"+"Otieno", "0788934537", "Y")
		result = len(allocations)
		office.allocate_to(fellow)
		result_1 = len(allocations)
		self.assertEqual(result+1, result_1)

	def test_allocate_to_existing_staff_space(self):
		office = Office("staff"+"Focuspo")
		staff = Staff("staff"+"Nerits", "staff"+"Oteno", "0784334222", "N")
		office.allocate_to(staff)
		with self.assertRaises(ValueError):
			office.allocate_to(staff)

	def test_allocate_to_staff_no_space(self):
		office = Office("staff"+'Focusp')
		with self.assertRaises(ValueError):
			x = 0
			while (x <= 5):
				suffix = str(x)
				staff = Staff("staff"+"Neris"+suffix, "staff"+"Oten"+suffix, "078433448"+suffix,"N")
				office.allocate_to(staff)
				x += 1

	def test_arrogate_from_existing_staff(self):
		office = Office("staff"+'Focs')
		staff = Staff("staff"+"Erits", "staff"+"Teno", "0785534224", "Y")
		office.allocate_to(staff)
		allocated_1 = office.has_allocation(staff)
		office.arrogate_from(staff)
		allocated_2 = office.has_allocation(staff)
		self.assertEqual([allocated_1, allocated_2], [True, False])

	def test_add_office(self):
		office = Office('MyOffice78')
		initial_room_count = len(Dojo.rooms())
		initial_office_count = len(Office.rooms())
		Office.add(office)
		new_room_count = len(Dojo.rooms())
		new_office_count = len(Office.rooms())
		self.assertEqual([initial_room_count+1, initial_office_count+1],
						 [new_room_count, new_office_count])

	def test_add_an_existing_office(self):
		office = Office('MyOffice4545')
		Office.add(office)
		with self.assertRaises(ValueError):
			Office.add(office)
	
	def test_remove_office(self):
		office = Office('MyOffice89')
		Office.add(office)
		initial_room_count = len(Dojo.rooms())
		initial_office_count = len(Office.rooms())
		print(Office.rooms())
		Office.remove(office)
		new_room_count = len(Dojo.rooms())
		new_office_count = len(Office.rooms())
		print(Office.rooms())
		self.assertEqual([initial_room_count-1, initial_office_count-1],
						 [new_room_count, new_office_count])


if __name__ == '__main__':
    main()