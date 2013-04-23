from agenda import *

book=ContactBook()
#book.loadContacts()
#book.saveContact("pancho","984589y85")
toRemove=Contact("pato","2405")
book.remContact(toRemove)


for  contact in book.book:
	print contact.name

#toRemove=Contact("pancho","894320")


#book.remContact(toRemove)
#print "remover!"
#for  contact in book.book:
#	print contact.name