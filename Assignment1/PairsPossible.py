from Assignment1.StringClass import StringClass


class PairsPossible(StringClass):
    __pair_list = []

    def all_possible_pairs(self):
        input_string = self.get_str()
        self.__pair_list = [[a, b] for idx, a in enumerate(input_string) for b in input_string[idx + 1:]]

    def get_all_possible_pairs(self):
        return self.__pair_list

    def print_pairs(self):
        for i in self.__pair_list:
            print(i, end=" ")
        print()
