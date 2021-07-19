import os
from customer import Customer 
from file_parser import FileParser

class UserMenu():

    def clearscreen(self):
        os.system('cls')

    def do_user_menu(self, ds):

        selection = "0"

        while(selection != "4"):
            self.clearscreen()
            selection = self.show_user_menu(ds)

            if(selection not in ["1", "2", "3", "4"]):
                self.clearscreen()
                print(f"Invalid menu option [{selection}]. Press return to try again.")
                input()

        # application is now exiting - write customers list to file
        file_parser = FileParser()

        file_parser.write_customers("custs.txt", ds.customers)



    def show_user_menu(self, ds):

        print(f"Welcome!")
        print("Menu options:")
        print("1. View existing Customers")
        print("2. Add Customer")
        print("3. Update Customer balance")
        print("4. Exit\n")
        selection = input("Please choose an option (1-4): ")

        if(selection == "1"):
            self.view_customers(ds)

        elif(selection == "2"):
            self.add_customer(ds)

        elif(selection == "3"):
            self.update_customer_balance(ds)

        return selection

    def view_customers(self, ds):
        self.clearscreen()
        print("ID    Forename   Surname    Phone No.  Email Address                  Postcode   Balance")
        print("===========================================================================================")

        for customer in ds.customers:
            print(customer)

        print("Return to continue...")
        input()        

    def add_customer(self, ds):
        print("Add a new Customer")
        print("==================\n")
        forename = input("Forename: ")
        surname = input("Surname: ")
        phone_number = input("Phone Number: ")
        email_address = input("Email Address: ")
        postcode = input("Postcode: ")

        balance = False
        while balance == False:
            try:
                balance = float(input("Initial Balance: "))
            except:
                print("Invalid balance. Please enter a numeric value...")

        customer = Customer(forename, surname, phone_number, email_address, postcode, balance)

        ds.add_customer(customer)

        print("Return to continue...")
        input()

    def update_customer_balance(self, ds):

        print("Update Customer Balance:")
        print("=======================\n")

        found_customer = False

        id = self.prompt_for_customer_id()

        for customer in ds.customers:
            if customer.id == id :
                found_customer = True

                # print some info about this customer
                print(f"Customer id: {customer.id} - {customer.forename} {customer.surname} - Current Balance: {customer.balance}")
                # update balance

                # get new balance
                new_balance = self.prompt_for_balance()

                # update customer
                customer.balance = new_balance

                #print(f"Customer id {id} - balance set to {new_balance}")
                print(f"Customer id: {customer.id} - {customer.forename} {customer.surname} - New Balance: {customer.balance}")
                input("Press return to continue: ")
        
        if found_customer == False:
            print(f"Could not find a customer with id = {id}. Please try again...")
            input("Press return to continue: ")


    def prompt_for_balance(self):

        balance_valid = False

        while balance_valid == False:
            try:
                balance = float(input("Please enter the new balance: "))
            except ValueError:
                print("Balance must be a floating point figure")
            else:
                balance_valid = True

        return balance

    def prompt_for_customer_id(self):

        id_valid = False 

        while id_valid == False:
            try:
                id = int(input("Please enter the Customer's id: "))
            except ValueError:
                print("Customer id must be a numeric value")
            else:
                id_valid = True

        return id


