"""
A menu - you need to add the database and fill in the functions. 
"""
from peewee import *

db = SqliteDatabase('chainsaw_records.sqlite')

class Record(Model):
    name = CharField()
    country = CharField()
    number_of_catches = IntegerField()

    class Meta:
        database = db
    
    def __str__(self):
        return f'{self.name}, {self.country}, {self.number_of_catches}'
db.connect()
db.create_tables([Record])


def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    records = Record.select()
    for record in records:
        print(record)


def add_new_record():
    holder_name = input('What is the name of the record holder? ')

    if Record.get_or_none(name = holder_name):
        print(f'{holder_name} has already been added to the records.')
    
    else:
        country_of_holder = input('What is the country of the holder? ')
        record_catches = int(input('What is the number of catches? '))
        holder_name = Record(name = holder_name, country = country_of_holder, number_of_catches = record_catches)
        holder_name.save()
        print(f'{holder_name} has been added to the records!')



def edit_existing_record():
    record_to_edit = input('Please enter the name of the record holder to edit: ')

    if Record.get_or_none(name = record_to_edit):
        new_record = int(input('Please enter a new record: '))
        Record.update(number_of_catches = new_record).where(Record.name == record_to_edit).execute()
        print('Record has been updated. ')

    else: 
        print('Record not found.')
    




def delete_record():
    record_to_delete = input('Please enter the record holder name to delete the record: ')

    if Record.get_or_none(name = record_to_delete):
        Record.delete().where(Record.name == record_to_delete).execute()
        print(f'{record_to_delete} has been deleted from the records.')
    else:
        print('Record not found.')
    

if __name__ == '__main__':
    main()