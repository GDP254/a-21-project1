#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

from models.dojo import Dojo
from models.room import Room
from models.office import Office
from models.livingspace import LivingSpace
from models.person import Person
from models.fellow import Fellow
from models.staff import Staff
from models.state import persons_phone

class TestReallocate(TestCase):

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

	def test_reallocate_existing_staff_to_office(self):
		office = Office('My9994')
		Office.add(office)
		staff = Staff("Ugeg", "Insdnis", "073437")
		office.allocate_to(staff)
		with self.assertRaises(ValueError):
			Room.reallocate(staff, office)

	def test_reallocate_staff_to_office(self):
		office = Office('Myok848')
		Office.add(office)
		staff = Staff("UNidng", "Inignis", "07089797537")
		office.allocate_to(staff)
		office1 = Office('M949438')
		Office.add(office1)
		Room.reallocate(staff, office1)
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
		fellowx = Fellow("UNjlksd", "Ilnjndis", "070000345537", "N")
		office.allocate_to(fellowx)
		office1 = Office('M94llj87')
		Office.add(office1)
		fellow = Fellow("Usdsd", "Isdsds", "070015837", "N")
		office1.allocate_to(fellow)
		fellow = Fellow("rereed", "Iererds", "234235837", "N")
		office1.allocate_to(fellow)
		fellow = Fellow("Usdsdfsd", "Iskops", "079879787", "N")
		office1.allocate_to(fellow)
		fellow = Fellow("Uhoidfd", "Ioijfdsoids", "089437237", "N")
		office1.allocate_to(fellow)
		with self.assertRaises(ValueError):
			Room.reallocate(fellowx, office1)
		self.assertEqual([office1.has_allocation(fellowx), office.has_allocation(fellowx)], 
						 [False, True])

if __name__ == '__main__':
    main()