#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main
import os

from app.controller import load_people
from app.controller import save_state
from app.controller import load_state
from app.models.dojo import Dojo
from app.models.room import Room
from app.models.livingspace import LivingSpace
from app.models.person import Person
from app.models.fellow import Fellow
from app.models.staff import Staff
from app.models.office import Office
from app.models.state import persons_phone

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