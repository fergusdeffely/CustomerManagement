import os
from customer import Customer 

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


    def show_user_menu(self, ds):

        print(f"Welcome!")
        print("Menu options:")
        print("1. View existing Customers")
        print("2. Add Customer")
        print("3. Exit\n")
        selection = input("Please choose an option (1-5): ")

        if(selection == "1"):
            self.clearscreen()
            print("Forename   Surname    Phone No.  Email Address                  Postcode")
            print("========================================================================")

            for customer in ds.customers:
                print(customer)

            print("Return to continue...")
            input()

        elif(selection == "2"):
            print("Add a new Customer")
            print("==================\n")
            forename = input("Forename: ")
            surname = input("Surname: ")
            phone_number = input("Phone Number: ")
            email_address = input("Email Address: ")
            postcode = input("Postcode: ")

            customer = Customer(forename, surname, phone_number, email_address, postcode)

            ds.add_customer(customer)

            print("Return to continue...")
            input()            

        return selection
