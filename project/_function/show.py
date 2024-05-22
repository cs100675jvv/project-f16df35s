from datetime import datetime
from _decorator.decorator import input_error_name, input_error_name
from _function.upcoming_birthdays import get_upcoming_birthdays
from _classes.adress_book import AddressBook



@input_error_name
def show_phone (args, book: 'AddressBook'):
    name, *_ = args
    record = book.find(name)
    if record:
        return f"Contact {name} has phone: {'; '.join(str(p) for p in record.phones)}"
    else:
        return f"Contact {name} not found in our dictionary."


def show_all(book: 'AddressBook'):
    result = []
    for name, phone, email, address in book.items():
        result.append(f"{name}: {phone}: {email}: {address}")
    return '\n'.join(result)

@input_error_name
def show_birthday(args, book: 'AddressBook'):
    name, *_ = args
    record = book.find(name)
    if record:
        date_obj = datetime.strptime(str(record.birthday), "%Y-%m-%d %H:%M:%S")
        return print(f"Contact {name} has birthday: {date_obj.strftime('%d-%m-%Y')}")
    else:
        return print(f"Contact {name} not found in our dictionary.")

def birthdays(book: 'AddressBook'):
    birthdays = get_upcoming_birthdays(book)
    for birthday in birthdays:
        print(birthday)