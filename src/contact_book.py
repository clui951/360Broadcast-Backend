### dictionary mapping users to their contact list ###

class ContactBook(object):

	def __init__(self):
		# maps user to list of contacts
		self.dictionary = {}


	def newUser(user):
		self.dictionary[user] = []


	def addContact(user, contact):
		contactLst = self.dictionary[user]
		contactLst.append(contact)


	def removeContact(user, contact):
		contactLst = self.dictionary[user]
		contactLst.remove(contact)


	def userExists(user):
		return user in self.dictionary


	def clearContacts(user):
		self.dictionary.pop(user, None)