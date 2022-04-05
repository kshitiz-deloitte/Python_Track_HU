from Assignment1.EqualSumPairs import EqualSumPairs
from Assignment1.PairsPossible import PairsPossible

if __name__ == '__main__':
    string_obj = PairsPossible()
    print("Length=", string_obj.get_length())
    string_obj.all_possible_pairs()
    equal_sum_paris = EqualSumPairs()
    equal_sum_paris.count_pair_with_distinct_sum(string_obj)
    equal_sum_paris.print_count()

