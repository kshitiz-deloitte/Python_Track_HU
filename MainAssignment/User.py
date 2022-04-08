from time import sleep

from Utils.readCfg import get_from_config


class User:
    __SECTION = "user"
    __COM_SECTION = "common_attribute"

    def __init__(self):
        print("******Welcome to BookMyShow*******")
        print(get_from_config(self.__SECTION, "user_login_options"))
        ch = int(input(get_from_config(self.__COM_SECTION, "enter_option")))
        flag = True
        while flag:
            if ch == 1:
                self.user_login()
            elif ch == 2:
                self.user_register()
            elif ch == 3:
                sleep(5000)
                print("Logging out")
                flag = False
            else:
                print("invalid input")

    def user_login(self):
        print("******Welcome to BookMyShow*******")
        user_name_log = input("User: ")
        user_pwd_log = input("Password: ")
        print("Login")

    def user_register(self):
        print("****Create new Account*****")
        user_name_reg = input("Name: ")
        user_email_reg = input("Email: ")
        user_ph_reg = input("Phone: ")
        user_pwd_reg = input("Password: ")

