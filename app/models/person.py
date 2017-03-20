from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.models.state import persons_detail, persons_phone

"""Narrative

Persons are either Staff or Fellow at the Dojo.
They can have unique phone numbers, two names and a indicator of type
 i.e. Office/ LivingSpace.
"""

Base = declarative_base()

class Person(Base):

	first_name = None
	last_name = None
	phone = None
	type_ = "Person"

	__tablename__ = "persons"

	id_ = Column(Integer, primary_key=True)
	phonenumber = Column(String(25), unique=True)
	firstname = Column(String(25))
	lastname = Column(String(25))
	role = Column(String(25))
	optin = Column(String(1))

	def __init__(self, first_name, last_name, phone, opt_in="N"):
		phone = phone.replace(" ", "")
		if phone.isdigit() is False:
			raise ValueError("The phone number provided %s is invalid" % phone)
		input_ = [first_name, last_name, phone]
		if "" or None in input_:
			raise ValueError("Please enter required information correctly and in full")
		first_name = str(first_name)
		last_name = str(last_name)
		names = [first_name, last_name]
		for name in names:
			if len(name) > 25:
				raise ValueError("Name too long. Please enter a shorter name")
		name_index = 0
		while name_index <= 1:
			names[name_index] = names[name_index].replace(" ", "")
			names[name_index] = names[name_index].upper()
			name_index += 1
		if opt_in not in ["y", "Y", "n", "N"]:
			opt_in = "N"
		if opt_in is not None:
			opt_in = opt_in.upper()
		self.first_name = names[0]
		self.last_name = names[1]
		self.phone = str(phone)
		self.opt_in = opt_in
		#db
		self.phonenumber = self.phone
		self.firstname = self.first_name
		self.lastname = self.last_name
		self.role = self.type_
		self.optin = self.opt_in

	#alternate constructor
	@classmethod
	def from_phone(cls, phone):
		"""To Do

		Retrieve detail recor of phone and initialize based on the information
		"""
		if phone in persons_phone:
			info = persons_detail[phone]
			first_name = info[0]
			last_name = info[1]
			type_ = info[2]
			opt_in = info[3]
			person = cls(first_name, last_name, phone, opt_in)
			person.type_ = type_
			person.role = type_
			return person
		else:
			raise ValueError("Specified phone does not exist")

	@classmethod
	def save_state(cls, file_name="default"):
		path = "db/"
		file_ = file_name+".db"
		engine = create_engine("sqlite:///"+path+file_, echo=False)
		cls.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)
		session = Session()
		for phone in persons_phone:
			#Create new instance of person
			firstname = persons_detail[phone][0]
			lastname = persons_detail[phone][1]
			type_ = persons_detail[phone][2]
			optin = persons_detail[phone][3]
			new_person = cls(firstname, lastname, phone, optin)
			new_person.type_ = type_
			new_person.role = type_
			session.add(new_person)
		session.commit()
		session.close()

	@classmethod
	def load_state(cls, file_name="default"):
		cls.clear()
		path = "db/"
		file_ = file_name+".db"
		engine = create_engine("sqlite:///"+path+file_, echo=False)
		Session = sessionmaker(bind=engine)
		session = Session()
		person_info = session.query(Person).all()
		for person in person_info:
			persons_phone.add(person.phonenumber)
			persons_detail.update({person.phonenumber:[person.firstname,
														person.lastname,
														person.role,
														person.optin]})
		session.close()
	
	def register(self):
		if self.registered():
			raise ValueError("Specifed phone is already registered")
		persons_phone.add(self.phone)
		persons_detail.update ({self.phone:[self.first_name, 
									self.last_name, 
									self.type_,
									self.opt_in]})

	def registered(self):
		if self.phone in persons_phone:
			return True
		return False

	@classmethod
	def clear(cls):
		"""To Do

		Clear all data stores relevant to persons for testing purposes
		"""

		persons_detail.clear()
		persons_phone.clear()