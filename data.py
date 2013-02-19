class base():
	def __init__(self,email=None):
		self.email=email

class basic_contact(base):
    def __init__(self, email=None, first_name=None, last_name=None):
    	self.email = email
        self.first_name = first_name
        self.last_name = last_name

class contact_work(base):
	def __init__(self, email=None, job=None, company=None, work_phone=None):
		self.email = email
		self.job = job
		self.company = company
		self.work_phone = work_phone

class contact_family(base):
	def __init__(self, email = None, home_phone=None, address1 = None,
				 address2 = None, address3 = None, city = None, state = None,
				 other_state=None, country = None, zipcode = None, subzipcode = None ):
		self.email = email
		self.home_phone = home_phone
		self.address1 = address1
		self.address2 = address2
		self.address3 = address3
		self.city = city
		self.state = state
		self.other_state = other_state
		self.country = country
		self.zipcode = zipcode

class contact_note(base):
	def __init__(self, email = None, note = None):
		self.email = email
		self.note = note

		
        


		