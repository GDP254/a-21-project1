#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

from controller import load_people
from models.dojo import Dojo
from models.room import Room
from models.livingspace import LivingSpace
from models.person import Person
from models.fellow import Fellow
from models.staff import Staff
from models.office import Office
from models.state import persons_phone

class TestController(TestCase):

	def test_load_people_valid_path(self):
		self.clear_stores()
		path = "test_in"
		load_people(path)
		output = persons_phone
		#test_in.txt has the following content
		expected_out =  set(["075588228", "5221455", "6655255", "1515151"])
		self.assertEqual(expected_out, output)

	def test_load_people_valid_path(self):
		self.clear_stores()
		expected_out = persons_phone
		path = "nothing_to_load"
		load_people(path)
		output = persons_phone
		self.assertEqual(expected_out, output)

	def clear_stores(self):
		#Clean data stores to run print tests
		Dojo.clear()
		Room.clear()
		Person.clear()

if __name__ == '__main__':
    main()