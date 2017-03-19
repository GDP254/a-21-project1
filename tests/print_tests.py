#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

from models.dojo import Dojo
from models.room import Room
from models.office import Office
from models.livingspace import LivingSpace
from models.fellow import Fellow
from models.staff import Staff
from models.person import Person

class TestPrint(TestCase):

	def test_print_populated_room(self):
		self.clear_stores()
		office = Office("NDO")
		Dojo.add_room(office)
		fellow = Fellow("Xone", "Ndobile", "0856443334", "y")
		fellow.register()
		office.allocate_to(fellow)
		allocations = office.allocations()
		output = Room.members(allocations)
		self.assertEqual(output, " 0856443334, NDOBILE, XONE, FELLOW\n")

	def test_print_empty_room(self):
		self.clear_stores()
		livingspace = LivingSpace("NDO1")
		with self.assertRaises(Exception):
			output = livingspace.allocations()

	def test_print_existing_allocations_to_screen(self):
		self.clear_stores()
		office = Office("NDO2")
		Dojo.add_room(office)
		fellow = Fellow("Xone2", "Ndobile2", "0856443324", "y")
		fellow.register()
		office.allocate_to(fellow)
		allocations_ = Room.all_allocations()
		output = Room.members(allocations_, room_tag=True)
		expected_output = " NDO2-OFFICE, 0856443324, NDOBILE2, XONE2, FELLOW\n"
		self.assertEqual(output, expected_output)

	def test_print_existing_allocations_to_default_file(self):
		self.clear_stores()
		office = Office("ND2")
		Dojo.add_room(office)
		fellow = Fellow("Xne2", "Ndoile2", "0868443324", "y")
		fellow.register()
		office.allocate_to(fellow)
		allocations_ = Room.all_allocations()
		expected_output = Room.members(allocations_, room_tag=True)
		Room.to_file(expected_output)
		path = "output/"
		f = open(path+"File.txt", "r")
		output = f.read() #"NDO2-Office, 0856443324, NDOBILE2, XONE2, FELLOW"
		f.close()
		self.assertEqual(expected_output, output)

	def test_print_existing_allocations_to_specific_file(self):
		self.clear_stores()
		office = Office("ND88")
		Dojo.add_room(office)
		fellow = Fellow("Xne88", "Ndoile88", "086800000", "y")
		fellow.register()
		office.allocate_to(fellow)
		allocations_ = Room.all_allocations()
		expected_output = Room.members(allocations_, room_tag=True)
		file_name = office.name+"-Allocations"
		Room.to_file(expected_output, file_name)
		path = "output/"
		f = open(path+file_name+".txt", "r")
		output = f.read() 
		f.close()
		self.assertEqual(expected_output, output)

	def test_print_existing_unallocated_to_screen(self):
		self.clear_stores()
		office = Office("NDO4")
		Dojo.add_room(office)
		fellow = Fellow("Xone4", "Ndobile4", "0856443354", "y")
		fellow.register()
		office.allocate_to(fellow)
		fellow = Fellow("Xone5", "Ndobile6", "0856443009", "n")
		fellow.register()
		office.allocate_to(fellow)
		fellow = Fellow("Xone3", "Ndobile3", "0856443344", "y")
		fellow.register()
		output = Room.all_unallocated_persons()
		expected_output = "0856443344, NDOBILE3, XONE3, FELLOW\n"
		self.assertEqual(output, expected_output)

	def clear_stores(self):
		#Clean data stores to run print tests
		Dojo.clear()
		Room.clear()
		Person.clear()

if __name__ == '__main__':
    main()
