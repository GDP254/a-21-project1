#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

class TestPerson(TestCase):

	def test_instantiate_room_from_name(self):
		livingspace  = LivingSpace('MyLLLLL')
		LivingSpace.add(livingspace)
		office = Office('MyJJJSS')
		Office.add(office)
		livingspace1 = LivingSpace.from_name("MyLLLLL")
		office1 = Office.from_name("MyJJJSS")
		self.assertEqual(office.name, office1.name)

	def test_reallocate_fellow_to_livingspace(self):
		livingspace  = LivingSpace('My9990')
		LivingSpace.add(livingspace)
		fellow = Fellow("jjjsj", "lksls", "07009987", "Y")
		livingspace.allocate_to(fellow)
		livingspace1  = LivingSpace('My9991')
		LivingSpace.add(livingspace1)
		Room.reallocate(fellow, livingspace1)
		self.assertEqual([livingspace1.has_allocation(fellow), livingspace.has_allocation(fellow)],
						 [True, False])

	def test_reallocate_staff_to_office(self):
		office = Office('Myok848')
		Office.add(office)
		staff = Staff("UNidng", "Inignis", "07089797537")
		office.allocate_to(staff)
		office1 = Office('M949438')
		Office.add(office1)
		Room.reallocate(fellow, office1)
		self.assertEqual([office1.has_allocation(staff), office.has_allocation(staff)], 
						 [True, False])

	def test_reallocate_staff_to_livingspace(self):
		office = Office('M777848')
		Office.add(office)
		staff = Staff("jjjkkdsj", "liidsls", "0799034987")
		office.allocate_to(staff)
		livingspace1 = LivingSpace('U988934')
		LivingSpace.add(livingspace1)
		with self.assertRaises(Exception):
			Room.reallocate(staff, livingspace1)

	def test_reallocate_fellow_to_office(self):
		office = Office('000848')
		Office.add(office)
		fellow = Fellow("UNlsldg", "Ilslnis", "070555597537", "N")
		office.allocate_to(fellow)
		office1 = Office('M9498987')
		Office.add(office1)
		Room.reallocate(fellow, office1)
		self.assertEqual([office1.has_allocation(fellow), office.has_allocation(fellow)], 
						 [True, False])

	def test_reallocate_to_room_at_capacity(self):
		office = Office('0884oo848')
		Office.add(office)
		fellow = Fellow("UNjlksd", "Ilnjndis", "070000345537", "N")
		office.allocate_to(fellow)
		office1 = Office('M9498987')
		Office.add(office1)
		fellow = Fellow("Usdsd", "Isdsds", "070015837", "N")
		office1.allocate_to(fellow)
		fellow = Fellow("rereed", "Iererds", "234235837", "N")
		office1.allocate_to(fellow)
		fellow = Fellow("Usdsdfsd", "Iskops", "079879787", "N")
		office1.allocate_to(fellow)
		fellow = Fellow("Uhoidfd", "Ioijfdsoids", "089437237", "N")
		office1.allocate_to(fellow)
		with self.assertRaises(Exception):
			Room.reallocate(fellow, office1)
		self.assertEqual([office1.has_allocation(fellow), office.has_allocation(fellow)], 
						 [False, True])

	def test_load_people_invalid_path(self):
		path = "bull"
		with self.assertRaises(Exception):
			Room.load_people(path)

	def test_load_people_valid_path(self):
		self.clear_stores()
		path = "input/test_in.txt"
		Room.load_people(path)
		output = person_phone
		expected_out =  set(["48845", "88555"])
		self.assertEqual(expected_out, output)

	def clear_stores(self):
		#Clean data stores to run print tests
		Dojo.clear()
		Room.clear()
		Person.clear()

if __name__ == '__main__':
    main()