#Interacting with the Shelf
import shelve
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'letters.txt')

db_file = shelve.open(file_path, 'c')
print ( list(db_file.keys( )))
print ("Original containing vowels:", 'vowels' in db_file )
del db_file ['vowels']
print ("After deleting vowels:", 'vowels' in db_file )
print ( list(db_file.keys( )))
db_file.close()
