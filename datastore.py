from customer import Customer

class Datastore:

    def __init__(self):

        self._customers = []
        
        self.load_customers()

    def load_customers(self):

        self._customers.append(Customer("Aaaaaa", "Bbbbbb", "0987654321", "aaaaaa.bbbbbb@test.org", "A12 BC34"))
        self._customers.append(Customer("Cccc", "Dddd", "1234567890", "cccc.dddd@test.org", "D56 EF78"))

    def add_customer(self, customer):

        self._customers.append(customer)


    @property
    def customers(self):
        return self._customers
