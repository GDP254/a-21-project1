#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

from models.fellow import Fellow
from models.staff import Staff
from models.state import persons_detail, persons_phone

class TestFellow(TestCase):

	"""
		Grouping: Attribute tests
		Description: The following tests confirm that necessary attributes exist
	"""

	def test_has_first_name(self):
		fellow = Fellow("Rando", "Dire", "0754838434", "Y")
		self.assertEqual(fellow.first_name, "RANDO")

	def test_has_last_name(self):
		fellow = Fellow("Randod", "Dired", "0994838434", "Y")
		self.assertEqual(fellow.last_name, "DIRED")

	def test_has_phone(self):
		fellow = Fellow("Randode", "Direde", "0794838434", "N")
		self.assertEqual(fellow.phone, "0794838434")

	def test_has_opt_in(self):
		fellow = Fellow("Randode", "Direde", "0794838434", "N")
		self.assertEqual(fellow.opt_in, "N")

	"""
		Grouping: Constructor input tests
		Description: The following tests confirm the constructor for instances of 
					Fellow respond appropriately to various input
	"""

	def test_constructor_no_argument(self):
		with self.assertRaises(TypeError):
			fellow = Fellow()

	def test_constructor_input_too_large(self):
		with self.assertRaises(ValueError):
			fellow = Fellow("Theraininspainstaysmainlyontheplainwashingawaythegrain", 
							"Diredes", "0794038434", "Y")

	def test_constructor_spaced_name(self):
		fellow = Fellow("ri ck", "Dir ede", "0794 838434", "Y")
		self.assertEqual([fellow.first_name, fellow.last_name, fellow.phone, fellow.opt_in], ["RICK", "DIREDE", "0794838434", "Y"])

	def test_constructor_upper(self):
		fellow = Fellow("Lolz", "Skid", "8483774855", "Y")
		self.assertEqual([fellow.first_name, fellow.last_name, fellow.phone, fellow.opt_in], ["LOLZ", "SKID", "8483774855", "Y"])

	"""
		Grouping: Register tests
		Description: The following tests confirm the save_state method of the
					class Fellow is functioning properly
	"""

	def test_register_phone_exists_error(self):
		fellow = Fellow("LIOLZ", "SKIDH", "8483664855", "Y")
		fellow.register()
		fellow_1 = Staff("LIOLZ", "SKIDH", "8483664855", "Y")
		with self.assertRaises(ValueError):
			fellow_1.register()
		
	def test_register_new_phone(self):
		fellow = Fellow("Standard", "SKIDH", "84900874855", "Y")
		initial_person_count = len(persons_detail)
		fellow.register()
		new_person_count = len(persons_detail)
		self.assertEqual(initial_person_count + 1, new_person_count)

	
if __name__ == '__main__':
    main()