#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main
from fellow_tests import TestFellow
from staff_tests import TestStaff

class TestAddPerson(TestCase):
	def test_add_person_successfully(self):
		TestFellow.test_save_state_new_phone()
		TestStaff.test_save_state_new_phone()
	
if __name__ == '__main__':
    main()