from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.models.room import Room
from app.models.state import allocations, allocations_set, allocations_name_type

Base = declarative_base()

"""Allocations (Many to Many Relationsip between persons and rooms)

This class is used to create instances of allocations to be stored in the database.
Given the the identifiers are custom i.e. phone number for person and room name for room,
I chose to avoid the work of mapping db generated identifiers and just have a table with 
my identifiers as expressed in memory due to time constraints.
"""

class Allocation(Base):

	__tablename__ = "allocations"

	id_ = Column(Integer, primary_key=True)
	roomname = Column(String(25))
	roomtype = Column(String(25))
	phonenumber = Column(String(25))

	def __init__(self, roomname, roomtype, phonenumber):
		self.roomname = roomname
		self.roomtype =  roomtype
		self.phonenumber = phonenumber

	@classmethod
	def save_state(cls, file_name="default"):
		allocations = Room.all_allocations()
		path = "db/"
		file_ = file_name+".db"
		engine = create_engine("sqlite:///"+path+file_, echo=False)
		cls.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)
		session = Session()
		for allocation_ in allocations:
			roomname = allocation_[0]
			roomtype = allocation_[1]
			phonenumber = allocation_[2]
			this_allocation = cls(roomname, roomtype, phonenumber)
			session.add(this_allocation)
		session.commit()
		session.close()

	@classmethod
	def load_state(cls, file_name="default"):
		Room.clear()
		path = "db/"
		file_ = file_name+".db"
		engine = create_engine("sqlite:///"+path+file_, echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		allocation_info = session.query(Allocation).all()
		for allocation_ in allocation_info:
			allocation = [allocation_.roomname, allocation_.roomtype, allocation_.phonenumber]
			allocation_str = "%s-%s-%s" % (allocation_.roomname, allocation_.roomtype, allocation_.phonenumber)
			allocation_name_type_str = "%s-%s" % (allocation_.roomname, allocation_.roomtype)
			allocations.append(allocation)
			allocations_name_type.append(allocation_name_type_str)
			allocations_set.add(allocation_str)
		session.close()


