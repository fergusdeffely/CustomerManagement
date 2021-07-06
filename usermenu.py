import os
from customer import Customer 
from file_parser import FileParser

class UserMenu():

    def clearscreen(self):
        os.system('cls')

    def do_user_menu(self, ds):

        selection = "0"

        while(selection != "3"):
            self.clearscreen()
            selection = self.show_user_menu(ds)

            if(selection not in ["1", "2", "3"]):
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
        print("3. Exit\n")
        selection = input("Please choose an option (1-3): ")

        if(selection == "1"):
            self.view_customers(ds)

        elif(selection == "2"):
            self.add_customer(ds)

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
