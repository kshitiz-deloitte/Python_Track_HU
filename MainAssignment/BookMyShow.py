import sys

from MainAssignment.Admin import Admin
from MainAssignment.User import User
from Utils.readCfg import get_from_config

__SECTION = "first_page"
__COM_SECTION = "common_attribute"

if __name__ == "__main__":
    while True:
        print("******Welcome to BookMyShow*******")
        print(get_from_config(__SECTION, "first_page_options"))
        ch = int(input(get_from_config(__COM_SECTION, "enter_option")))
        if ch == 1:
            Admin()
        elif ch == 2:
            User()
        else:
            sys.exit()
