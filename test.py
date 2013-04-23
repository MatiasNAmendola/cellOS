from agenda import *

book=ContactBook()
book.loadContacts()
#book.saveContact("pancho","984589y85")


for  i in range(10):

	print book.navContact(True).name