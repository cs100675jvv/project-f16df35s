from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        if not self.value.strip():
            raise ValueError("Name cannot be empty.")


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    # def validate(self):
    #     if not re.match(r'^\d{10}$', self.value):
    #         raise ValueError("Invalid phone number format. Phone number should contain 10 digits.")


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        try:
            self.value = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Email(Field):
    def __init__(self, value):
        super().__init__(value)

class Address(Field):
    def __init__(self, value):
        super().__init__(value)
