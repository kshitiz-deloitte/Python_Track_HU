class EqualSumPairs:
    __count = 0

    def __init__(self):
        self.count = 0

    def count_pair_with_distinct_sum(self, pair_object):
        sum_list = {}
        for i in pair_object.get_all_possible_pairs():
            pair_sum = 0
            for k in i:
                pair_sum += int(k)
            if pair_sum in sum_list:
                sum_list[pair_sum] += 1
            else:
                sum_list[pair_sum] = 1
        for key, value in sum_list.items():
            if value == 1:
                self.__count += 1

    def print_count(self):
        print(self.__count)
