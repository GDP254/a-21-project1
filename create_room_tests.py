#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main

from office_tests import TestOffice
from livingspace_tests import TestLivingSpace

class TestCreateRoom(TestCase):
	def test_create_room_successfully(self):
		TestOffice.test_save_state_new_room()
		TestLivingSpace.test_save_state_new_room()
	
if __name__ == '__main__':
    main()