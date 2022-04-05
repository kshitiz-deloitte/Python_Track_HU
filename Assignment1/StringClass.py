class StringClass:
    __input_str = ""

    def __init__(self):
        self.__input_str = input("Enter the String:")

    def get_length(self):
        return len(self.__input_str)

    def convert_into_list_char(self):
        return list(self.__input_str)

class PairsPossible(StringClass):
    __pair_list = []

    def possible_pairs(self, char_list):
        self.__pair_list = [(a, b) for idx, a in enumerate(char_list) for b in char_list[idx + 1:]]

    def print_pairs(self):
        for i in self.__pair_list:
            print(i, end=" ")

# class SearchCommonElements:
#     def


string_obj = PairsPossible()
print(string_obj.get_length())
string_obj.possible_pairs(string_obj.convert_into_list_char())
string_obj.print_pairs()