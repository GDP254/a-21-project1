#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main

class TestFellow(TestCase):

	def test_has_first_name(self):
		fellow = Fellow("Rando", "Dire", "0754838434", "Y")
		self.assertEquals(fellow.first_name, "Rando")

	def test_has_last_name(self):
		fellow = Fellow("Randod", "Dired", "0994838434", "Y")
		self.assertEquals(fellow.last_name, "Dired")

	def test_has_phone(self):
		fellow = Fellow("Randode", "Direde", "0794838434", "N")
		self.assertEquals(fellow.phone, "0794838434")

	def test_has_choice(self):
		fellow = Fellow("Randode", "Direde", "0794838434", "N")
		self.assertEquals(fellow.choice, "N")

	def test_constructor_no_argument(self):
		with self.assertRaises(ValueError):
			fellow = Fellow()

	def test_constructor_empty_string(self):
		with self.assertRaises(ValueError):
			fellow = Fellow("","","","")

	def test_constructor_none(self):
		with self.assertRaises(ValueError):
			fellow = Fellow(None, None, None, None)

	def test_constructor_special_characters(self):
		with self.assertRaises(ValueError):
			fellow = Fellow("@*$(£&$", "@*$(£&$", "@*$(£&$","N")

	def test_constructor_input_too_large(self):
		with self.assertRaises(ValueError):
			fellow = Fellow("Theraininspainstaysmainlyontheplainwashingawaythegrain", 
							"Diredes", "0794038434", "Y")

	def test_constructor_spaced_name(self):
		with self.assertRaises(ValueError):
			fellow = Fellow("ri ck", "Dir ede", "0794 838434", "Y")

	def test_constructor_positive_integer(self):
		with self.assertRaises(ValueError):
			fellow = Fellow(43, 56, "0794838434", "N")

	def test_constructor_positive_float(self):
		with self.assertRaises(ValueError):
			fellow = Fellow(4.3, "Direde", "0794838434", "N")

	def test_constructor_negative_integer(self):
		with self.assertRaises(ValueError):
			fellow = Fellow(-43, "Direde", "0794838434", "Y")

	def test_constructor_negative_float(self):
		with self.assertRaises(ValueError):
			fellow = Fellow(-4.3, "Direde", "0794838434", "N")

	def test_constructor_capitalize(self):
		fellow = Fellow("LOLZ", "SKID", "8483774855", "Y")
		self.assertEquals([fellow.first_name, fellow.second_name, fellow.phone, fellow.choice], ["Lolz", "Skid", "8483774855", "Y"])

	def test_save_state_phone_exists_error(self):
		fellow = Fellow("LIOLZ", "SKIDH", "8483774855", "Y")
		fellow.save_state()
		fellow_1 = Fellow("LIOZ", "SIDH", "8483774855", "Y")
		with self.assertRaises(ValueError):
			fellow_1.save_state()

	def test_save_state_phone_exists(self):
		fellow = Fellow("LIOLZ", "SKIDH", "8483774855", "Y")
		initial_person_count = len(State.persons)
		fellow.save_state()
		fellow_1 = Fellow("LIOZ", "SIDH", "8483874855", "Y")
		fellow_1.save_state()
		new_person_count = len(State.persons)
		self.assertEquals(initial_person_count, new_person_count)

	def test_save_state_new_phone(self):
		fellow = Fellow("Standard")
		initial_person_count = len(State.persons)
		fellow.save_state()
		new_person_count = len(State.persons)
		self.assertEquals(initial_person_count + 1, new_person_count)

	
if __name__ == '__main__':
    main()