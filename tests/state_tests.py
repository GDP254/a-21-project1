#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase, main
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.dojo import Dojo
from models.room import Room
from models.office import Office
from models.livingspace import LivingSpace
from models.person import Person
from models.fellow import Fellow
from models.staff import Staff
from models.state import persons_phone

class TestState(TestCase):

	def test_fellow_save_state(self):
		#memory
		fellow = Fellow("onon", "ekek", "774883838", "Y")
		fellow.register()
		Person.save_state()
		#db
		engine = create_engine("sqlite://:memory", echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_fellow = session.query(Persons).filter_by(phone="774883838").first()
		#compare
		full_fellow = [fellow.first_name, fellow.last_name, fellow.phone, fellow.opt_in]
		full_db_fellow = [db_fellow.first_name, db_fellow.last_name, db_fellow.phone, db_fellow.opt_in]
		self.assertEqual(full_fellow, full_db_fellow)

	def test_fellow_load_state(self):
		#db
		engine = create_engine("sqlite://:memory", echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_fellow = session.query(Persons).filter_by(phone="774883838").first()
		#memory
		Person.load_state()
		fellow = Fellow.from_phone("774883838")
		#compare
		full_fellow = [fellow.first_name, fellow.last_name, fellow.phone, fellow.opt_in]
		full_db_fellow = [db_fellow.first_name, db_fellow.last_name, db_fellow.phone, db_fellow.opt_in]
		self.assertEqual(full_db_fellow, full_fellow)

	def test_staff_save_state(self):
		#memory
		staff = Staff("onsn", "edsk", "46546412")
		staff.register()
		Person.save_state()
		#db
		engine = create_engine("sqlite://:memory", echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_staff = session.query(Persons).filter_by(phone="46546412").first()
		#compare
		full_staff = [staff.first_name, staff.last_name, staff.phone, staff.opt_in]
		full_db_staff = [db_staff.first_name, db_staff.last_name, db_staff.phone, db_staff.opt_in]
		self.assertEqual(full_staff, full_db_staff)

	def test_staff_load_state(self):
		#db
		engine = create_engine("sqlite://:memory", echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_staff = session.query(Persons).filter_by(phone="46546412").first()
		#memory
		Person.load_state()
		staff = Staff.from_phone("774883838")
		#compare
		full_staff = [staff.first_name, staff.last_name, staff.phone, staff.opt_in]
		full_db_staff = [db_staff.first_name, db_staff.last_name, db_staff.phone, db_staff.opt_in]
		self.assertEqual(full_db_staff, full_staff)

	def test_office_save_state(self):
		#memory
		office = Office('oomse89')
		Office.add(office)
		Office.save_state()
		#db
		engine = create_engine("sqlite://:memory", echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_office = session.query(Rooms).filter_by(name='oomse89').first()
		#compare
		full_office = [office.name, office.capacity, office.type]
		full_db_office = [db_office.name, db_office.capacity, db_office.type]
		self.assertEqual(full_db_office, full_office)

	def test_office_load_state(self):
		#db
		engine = create_engine("sqlite://:memory", echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_office = session.query(Rooms).filter_by(name='oomse89').first()
		#memory
		Office.load_state()
		office = Office.from_name('oomse89')
		#compare
		full_office = [office.name, office.capacity, office.type]
		full_db_office = [db_office.name, db_office.capacity, db_office.type]
		self.assertEqual(full_db_office, full_office)

	def test_livingspace_save_state(self):
		#memory
		livingspace = LivingSpace('ojsdj89')
		LivingSpace.add(livingspace)
		LivingSpace.save_state()
		#db
		engine = create_engine("sqlite://:memory", echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_livingspace = session.query(Rooms).filter_by(name='ojsdj89').first()
		#compare
		full_livingspace = [livingspace.name, livingspace.capacity, livingspace.type]
		full_db_livingspace = [db_livingspace.name, db_livingspace.capacity, db_livingspace.type]
		self.assertEqual(full_db_livingspace, full_livingspace)

	def test_livingspace_load_state(self):
		#db
		engine = create_engine("sqlite://:memory", echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_livingspace = session.query(Rooms).filter_by(name='ojsdj89').first()
		#memory
		LivingSpace.load_state()
		livingspace = LivingSpace.from_name('ojsdj89')
		#compare
		full_livingspace = [livingspace.name, livingspace.capacity, livingspace.type]
		full_db_livingspace = [db_livingspace.name, db_livingspace.capacity, db_livingspace.type]
		self.assertEqual(full_db_livingspace, full_livingspace)

	def test_allocations_save_state(self):
		#memory
		livingspace = LivingSpace('hwan')
		LivingSpace.add(livingspace)
		fellow = Fellow("onon", "ekek", "000009", "Y")
		fellow.register()
		livingspace.allocate_to(fellow)
		prev_allocations_count = len(Room.all_allocations())
		Room.save_state()
		#db
		engine = create_engine("sqlite://:memory", echo=True)
		Session = sessionmaker(bind=engine)
		session = Session()
		db_allocations_count = session.query(Allocations).filter_by(phone="000009").count()
		#compare
		full_allocations_count = len(Room.all_allocations()) - prev_allocations_count
		self.assertEqual(full_allocations_count, db_allocations_count)

if __name__ == '__main__':
    main()