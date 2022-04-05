from Assignment1.EqualSumPairs import EqualSumPairs
from Assignment1.PairsPossible import PairsPossible
from Assignment1.SearchCommonElements import SearchCommonElements

if __name__ == '__main__':
    string_obj = PairsPossible()
    print("Length=", string_obj.get_length())
    string_obj.all_possible_pairs()

    string_obj2 = SearchCommonElements()
    string_obj2.common_elements(string_obj)

    equal_sum_pairs = EqualSumPairs()
    equal_sum_pairs.count_pair_with_distinct_sum(string_obj)
    equal_sum_pairs.print_count()

