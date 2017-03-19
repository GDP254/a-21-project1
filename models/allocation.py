from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from models.room import Room
from models.state import allocations, allocations_set, allocations_name_type

Base = declarative_base()

class Allocation(Base):

	__tablename__ = "allocations"

	id_ = Column(Integer, primary_key=True)
	roomname = Column(String(25), unique=True)
	roomtype = Column(String(25))
	phonenumber = Column(String(25))

	def __init__(self, roomname, roomtype, phonenumber):
		self.roomname = roomname
		self.roomtype =  roomtype
		self.phonenumber = phonenumber

	@classmethod
	def save_state(cls):
		allocations = Room.all_allocations()
		engine = create_engine("sqlite:///db/mydb.db", echo=True)
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
	def load_state(cls):
		print("Allocation::::::LoadState______")
		Room.clear()
		engine = create_engine("sqlite:///db/mydb.db", echo=True)
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


