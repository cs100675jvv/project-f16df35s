import re
from datetime import datetime

class PhoneValidationError(ValueError):
    pass

class NameValidationError(ValueError):
    pass

class EmailValidationError(ValueError):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            name, phone = args[0]

            if not re.match(r'^[a-zA-Zа-яА-ЯїЇєЄіІёЁ]+$', name):
                raise NameValidationError

            if not re.match(r'^\d{10}$', phone):
                raise PhoneValidationError

            return func(*args, **kwargs)

        except PhoneValidationError:
            message = "Invalid phone number. Phone number should contain only digits and be at least 10 digits long."
        except NameValidationError:
            message = "Invalid name. Only letters (latin or cyrillic) are allowed."
        except KeyError:
            message = "Enter user name."
        except ValueError:
            message = "Give me name and phone please."
        except IndexError:
            message = "Missing arguments"
        except Exception as e:
            message = f"Error in {func.__name__}: {e}"
        return message

    return inner


def input_error_phones(func):
    def inner(*args, **kwargs):
        try:
            name, phone, new_phone, *_ = args[0]

            if not re.match(r'^\d{10,}$', phone):
                raise PhoneValidationError

            if not re.match(r'^\d{10}$', new_phone):
                raise PhoneValidationError

            return func(*args, **kwargs)

        except PhoneValidationError:
            message = "Invalid phone number. Phone number should contain only digits and be at least 10 digits long."
        except KeyError:
            message = "Enter user name."
        except ValueError:
            message = "Give me name and phones please."
        except IndexError:
            message = "Missing arguments."
        except Exception as e:
            message = f"Error in {func.__name__}: {e}"
        return message

    return inner


def input_error_birthday(func):
    def inner(*args, **kwargs):
        try:
            name, birthday, *_ = args[0]

            birthday_obj = datetime.strptime(birthday, '%d.%m.%Y')  # Перевірка та створення об'єкта дати
            current_year = datetime.now().year
            if birthday_obj.year < 1900 or birthday_obj.year > current_year:
                raise ValueError("Invalid year. Birth year should be between 1900 and current year.")

            return func(*args, **kwargs)

        except KeyError:
            message = "Enter user name."
        except ValueError:
            message = "Give me name and birthday please."
        except IndexError:
            message = "Missing arguments."
        except Exception as e:
            message = f"Error in {func.__name__}: {e}"
        return message

    return inner


def input_error_email(func):
    def inner(*args, **kwargs):
        try:
            name, email, *_ = args[0]

            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_regex, email):
                raise EmailValidationError

            return func(*args, **kwargs)

        except EmailValidationError:
            message = "Invalid email. Please, enter a real email."
        except KeyError:
            message = "Enter user name."
        except ValueError:
            message = "Give me name and email please."
        except IndexError:
            message = "Missing arguments."
        except Exception as e:
            message = f"Error in {func.__name__}: {e}"
        return message

    return inner


def input_error_emailes(func):
    def inner(*args, **kwargs):
        try:
            name, email, *_ = args[0]

            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            if not re.match(email_regex, email):
                raise EmailValidationError

            return func(*args, **kwargs)

        except EmailValidationError:
            message = "Invalid email. Please, enter a real email."
        except KeyError:
            message = "Enter user name."
        except ValueError:
            message = "Give me name and email please."
        except IndexError:
            message = "Missing arguments."
        except Exception as e:
            message = f"Error in {func.__name__}: {e}"
        return message

    return inner

def input_error_note(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except KeyError:
            message = "KeyError"
        except ValueError:
            message = "Please specify at least one argument"
        except IndexError:
            message = "Missing arguments"
        except Exception as e:
            message = f"Error in {func.__name__}: {e}"
        return message

    return inner
