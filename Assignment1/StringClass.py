class StringClass:
    __input_str = ""
    __char_list = []

    def __init__(self):
        self.__input_str = input("Enter the String:")

    def get_length(self):
        return len(self.__input_str)

    def convert_into_list_char(self):
        self.__char_list = list(self.__input_str)

    def get_char_list(self):
        return self.__char_list

    def get_str(self):
        return self.__input_str












