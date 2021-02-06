import sqlite3
import argparse

class Phonebook(object):
    def __init__(self):
        try:
            c.execute('CREATE TABLE entries(id INTEGER PRIMARY KEY,name TEXT, phone TEXT)')
        except:
            pass
        print('Welcome to the Phonebook')
        
    def addContact():
        name = input("enter a name")
        namber = input("enter a number")
        kolvoID = 1
        for i in c.execute('SELECT * FROM  entries'):
            kolvoID += 1
        try:
            c.execute("INSERT INTO entries VALUES(?,?,?)",(kolvoID,name,namber))
            db.commit()
        except sqlite3.IntegrityError:
            print("error")

    def deleteContact():
        name = input("enter the contact name to delete")
        c.execute("delete from entries where name=?', [name]")
        db.commit()

        
Phonebook()

parser = argparse.ArgumentParser(description='Phonebook')
parser.add_argument('-a','--addContact', action='store_true', help = 'add new contact')
parser.add_argument('-d','--deleteContact',action = 'store_true', help = 'delete a contact')
args = parser.parse_args()

if args.addContact:
    Phonebook.addContact()

if args.deleteContact:
    Phonebook.deleteContact()


db.close()
