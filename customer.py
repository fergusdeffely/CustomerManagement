# class Account:

#     def __init__(self):
#         self.name = "Test account"


class Customer:

    def __init__(self, forename, surname, phone_number, email_address, postcode):

        self._forename = forename
        self._surname = surname 
        self._phone_number = phone_number
        self._email_address = email_address
        self._postcode = postcode

    def __repr__(self):
        return f"{self.forename.ljust(10)} {self.surname.ljust(10)} {self.phone_number.ljust(10)} {self.email_address.ljust(30)} {self.postcode.ljust(10)}"

    @property
    def forename(self):
        return self._forename

    @forename.setter
    def forename(self, new_forename):
        self._forename = new_forename

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, new_phone_number):
        self._phone_number = new_phone_number

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        self.email_address = email_address

    @property
    def postcode(self):
        return self._postcode

    @postcode.setter
    def postcode(self, new_postcode):
        self._postcode = new_postcode