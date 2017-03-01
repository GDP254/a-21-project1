#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

class TestStaff(TestCase):

	def test_has_first_name(self):
		staff = Staff("Rando", "Dire", "0754838434")
		self.assertEquals(staff.first_name, "Rando")

	def test_has_last_name(self):
		staff = Staff("Randod", "Dired", "0994838434")
		self.assertEquals(staff.last_name, "Dired")

	def test_has_phone(self):
		staff = Staff("Randode", "Direde", "0794838434")
		self.assertEquals(staff.phone, "0794838434")

	def test_has_choice(self):
		staff = Staff("Randode", "Direde", "0794838434")
		self.assertEquals(staff.choice, "N")

	def test_constructor_no_argument(self):
		with self.assertRaises(ValueError):
			staff = Staff()

	def test_constructor_empty_string(self):
		with self.assertRaises(ValueError):
			staff = Staff("","","")

	def test_constructor_none(self):
		with self.assertRaises(ValueError):
			staff = Staff(None, None, None, None)

	def test_constructor_special_characters(self):
		with self.assertRaises(ValueError):
			staff = Staff("@*$(£&$", "@*$(£&$", "@*$(£&$")

	def test_constructor_input_too_large(self):
		with self.assertRaises(ValueError):
			staff = Staff("Theraininspainstaysmainlyontheplainwashingawaythegrain", 
							"Diredes", "0794038434")

	def test_constructor_spaced_name(self):
		with self.assertRaises(ValueError):
			staff = Staff("ri ck", "Dir ede", "0794 838434")

	def test_constructor_positive_integer(self):
		with self.assertRaises(ValueError):
			staff = Staff(43, 56, "0794838434")

	def test_constructor_positive_float(self):
		with self.assertRaises(ValueError):
			staff = Staff(4.3, "Direde", "0794838434")

	def test_constructor_negative_integer(self):
		with self.assertRaises(ValueError):
			staff = Staff(-43, "Direde", "0794838434")

	def test_constructor_negative_float(self):
		with self.assertRaises(ValueError):
			staff = Staff(-4.3, "Direde", "0794838434")

	def test_constructor_capitalize(self):
		staff = Staff("LOLZ", "SKID", "8483774855")
		self.assertEquals([fellow.first_name, fellow.second_name, fellow.phone, fellow.choice],
							["Lolz", "Skid", "8483774855", "Y"])

	def test_save_state_phone_exists_error(self):
		staff = Staff("LIOLZ", "SKIDH", "8483774855")
		staff.save_state()
		staff_1 = Staff("LIOZ", "SIDH", "8483774855")
		with self.assertRaises(ValueError):
			staff_1.save_state()

	def test_save_state_phone_exists(self):
		staff = Staff("LIOLZ", "SKIDH", "8483774855")
		initial_person_count = len(State.persons)
		staff.save_state()
		staff_1 = Staff("LIOZ", "SIDH", "8483874855")
		staff_1.save_state()
		new_person_count = len(State.persons)
		self.assertEquals(initial_person_count, new_person_count)

	def test_save_state_new_phone(self):
		staff = Staff("Standard")
		initial_person_count = len(State.persons)
		staff.save_state()
		new_person_count = len(State.persons)
		self.assertEquals(initial_person_count + 1, new_person_count)

	
if __name__ == '__main__':
    main()