from datastore import Datastore 
from usermenu import UserMenu 

datastore = Datastore()
user_menu = UserMenu()

user_menu.do_user_menu(datastore)
