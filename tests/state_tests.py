#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.dojo import Dojo
from models.room import Room
from models.office import Office
from models.livingspace import LivingSpace
from models.person import Person
from models.fellow import Fellow
from models.staff import Staff
from models.allocation import Allocation
from models.state import persons_phone

class TestState(TestCase):

	def test_fellow_save_state(self):
		#clean up to avoid conflict between tests
		os.remove("db/mydb.db")
		self.clear_stores()
		#memory
		fellow = Fellow("onon", "ekek", "774883838", "Y")
		fellow.register()
		Person.save_state()
		#db
		engine = create_engine("sqlite:///db/mydb.db", echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_fellow = session.query(Person).filter_by(phonenumber="774883838").first()
		#compare
		full_fellow = [fellow.first_name, fellow.last_name, fellow.phone, fellow.type_, fellow.opt_in]
		full_db_fellow = [db_fellow.firstname, db_fellow.lastname, db_fellow.phonenumber, db_fellow.role, db_fellow.optin]
		session.close()
		self.assertEqual(full_fellow, full_db_fellow)

	def test_fellow_load_state(self):
		#clean up to avoid conflict between tests
		os.remove("db/mydb.db")
		#clear memory stores
		self.clear_stores()
		#memory
		fellow1 = Fellow("osdflkjsd", "eksdlkfjk", "774881228", "Y")
		fellow1.register()
		Person.save_state()
		#memory
		Person.load_state()
		fellow = Fellow.from_phone("774881228")
		#db
		engine = create_engine("sqlite:///db/mydb.db", echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_fellow = session.query(Person).filter_by(phonenumber="774881228").first()
		session.close()
		#compare
		full_fellow = [fellow.first_name, fellow.last_name, fellow.phone, fellow.type_, fellow.opt_in]
		full_db_fellow = [db_fellow.firstname, db_fellow.lastname, db_fellow.phonenumber, db_fellow.role, db_fellow.optin]
		self.assertEqual(full_db_fellow, full_fellow)

	def test_staff_save_state(self):
		#clean up to avoid conflict between tests
		os.remove("db/mydb.db")
		self.clear_stores()
		#memory
		staff = Staff("onsn", "edsk", "46546412")
		staff.register()
		Person.save_state()
		#db
		engine = create_engine("sqlite:///db/mydb.db", echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_staff = session.query(Person).filter_by(phonenumber="46546412").first()
		#compare
		full_staff = [staff.first_name, staff.last_name, staff.phone, staff.type_, staff.opt_in]
		full_db_staff = [db_staff.firstname, db_staff.lastname, db_staff.phonenumber, db_staff.role, db_staff.optin]
		session.close()
		self.assertEqual(full_staff, full_db_staff)

	def test_staff_load_state(self):
		#clean up to avoid conflict between tests
		os.remove("db/mydb.db")
		self.clear_stores()
		#memory
		staff1 = Staff("kdjsn", "ejsjssk", "40000412")
		staff1.register()
		Person.save_state()
		#db
		engine = create_engine("sqlite:///db/mydb.db", echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_staff = session.query(Person).filter_by(phonenumber="40000412").first()
		#clear memory stores
		self.clear_stores()
		#memory
		Person.load_state()
		staff = Staff.from_phone("40000412")
		#compare
		full_staff = [staff.first_name, staff.last_name, staff.phone, staff.type_, staff.opt_in]
		full_db_staff = [db_staff.firstname, db_staff.lastname, db_staff.phonenumber, db_staff.role, db_staff.optin]
		session.close()
		self.assertEqual(full_db_staff, full_staff)


	def test_office_save_state(self):
		#clean up to avoid conflict between tests
		os.remove("db/mydb.db")
		self.clear_stores()
		#memory
		office = Office('oomse89')
		Office.add(office)
		Office.save_state()
		#db
		engine = create_engine("sqlite:///db/mydb.db", echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_office = session.query(Room).filter_by(roomname='oomse89'.upper()).first()
		#compare
		full_office = [office.name, office.capacity, office.type_]
		full_db_office = [db_office.roomname, db_office.roomcapacity, db_office.roomtype]
		session.close()
		self.assertEqual(full_db_office, full_office)

	def test_office_load_state(self):
		#clean up to avoid conflict between tests
		os.remove("db/mydb.db")
		self.clear_stores()
		#memory
		office1 = Office('ooskks9')
		Office.add(office1)
		Office.save_state()
		#db
		engine = create_engine("sqlite:///db/mydb.db", echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_office = session.query(Room).filter_by(roomname='ooskks9'.upper()).first()
		#clear memory stores
		self.clear_stores()
		#memory
		Office.load_state()
		office = Office.from_name('ooskks9')
		#compare
		full_office = [office.name, office.capacity, office.type_]
		full_db_office = [db_office.roomname, db_office.roomcapacity, db_office.roomtype]
		session.close()
		self.assertEqual(full_db_office, full_office)

	def test_livingspace_save_state(self):
		#clean up to avoid conflict between tests
		os.remove("db/mydb.db")
		self.clear_stores()
		#memory
		livingspace = LivingSpace('ojsdj89')
		LivingSpace.add(livingspace)
		LivingSpace.save_state()
		#db
		engine = create_engine("sqlite:///db/mydb.db", echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_livingspace = session.query(Room).filter_by(roomname='ojsdj89'.upper()).first()
		#compare
		full_livingspace = [livingspace.name, livingspace.capacity, livingspace.type_]
		full_db_livingspace = [db_livingspace.roomname, db_livingspace.roomcapacity, db_livingspace.roomtype]
		session.close()
		self.assertEqual(full_db_livingspace, full_livingspace)

	def test_livingspace_load_state(self):
		#clean up to avoid conflict between tests
		os.remove("db/mydb.db")
		self.clear_stores()
		#memory
		livingspace1 = LivingSpace('oju5nf89')
		LivingSpace.add(livingspace1)
		LivingSpace.save_state()
		#db
		engine = create_engine("sqlite:///db/mydb.db", echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_livingspace = session.query(Room).filter_by(roomname='oju5nf89'.upper()).first()
		#clear memory stores
		self.clear_stores()
		#memory
		LivingSpace.load_state()
		livingspace = LivingSpace.from_name('oju5nf89')
		#compare
		full_livingspace = [livingspace.name, livingspace.capacity, livingspace.type_]
		full_db_livingspace = [db_livingspace.roomname, db_livingspace.roomcapacity, db_livingspace.roomtype]
		session.close()
		self.assertEqual(full_db_livingspace, full_livingspace)

	def test_allocations_save_state(self):
		#clean up to avoid conflict between tests
		os.remove("db/mydb.db")
		self.clear_stores()
		#memory
		livingspace = LivingSpace('hwan')
		LivingSpace.add(livingspace)
		fellow = Fellow("onon", "ekek", "000009", "Y")
		fellow.register()
		livingspace.allocate_to(fellow)
		Allocation.save_state()
		#db
		engine = create_engine("sqlite:///db/mydb.db", echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_allocation = session.query(Allocation).first()
		#compare
		db_output = [db_allocation.roomname, db_allocation.roomtype, db_allocation.phonenumber]
		self.assertEqual(Room.all_allocations()[0], db_output)
		session.close()

	def test_allocations_load_state(self):
		#clean up to avoid conflict between tests
		os.remove("db/mydb.db")
		self.clear_stores()
		#memory
		livingspace = LivingSpace('hwan')
		LivingSpace.add(livingspace)
		fellow = Fellow("onon", "ekek", "000009", "Y")
		fellow.register()
		livingspace.allocate_to(fellow)
		prev_allocations = Room.all_allocations().copy()
		Allocation.save_state()
		#clear memory stores
		self.clear_stores()
		empty_allocations = Room.all_allocations().copy()
		#db
		Allocation.load_state()
		loaded_allocations = Room.all_allocations().copy()
		#compare
		expected_output = ["HWAN", "LIVINGSPACE", "000009"]
		output = [prev_allocations[0], empty_allocations, loaded_allocations[0]]
		self.assertEqual(output, [expected_output, [], expected_output])
	
	def clear_stores(self):
		#Clean data stores to run print tests
		Dojo.clear()
		Room.clear()
		Person.clear()

if __name__ == '__main__':
    main()
