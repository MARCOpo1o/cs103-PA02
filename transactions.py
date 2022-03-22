'''
in a new file transactions.py which will store financial 
transactions with the fields. It should have an __init__ method 
where you pass in the filename for the database to be used 
(e.g. tracker.db) and each transaction should have the following 
fields stored in a SQL table called transactions. 
The transaction class should not do any printing!! 
'item #','amount','category','date','description'

'''

class transactions():
    def __init__(filename):
        self.filename = filename
        