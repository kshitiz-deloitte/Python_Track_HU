TAG = "Solution for Problem:"

def prob1(prob_num, array_list):
    print(TAG, prob_num)
    for items in array_list:
        dct = {i: items.count(i) for i in items}
        for keys, value in dct.items():
            if value > 1:
                print(keys, "->", value, end=" ")
        print()


def prob2(prob_num, list1, list2):
    print(TAG, prob_num)
    fin_list = []
    for item in list1:
        for item2 in list2:
            fin_list.append(item+" "+item2)
    print(fin_list)


def iterate_nested_list(list1, sub_list):
    for item in list1:
        if type(item) is list:
            iterate_nested_list(item, sub_list)
            item += sub_list
            return


def prob3(prob_num, nested_list, sub_list):
    print(TAG, prob_num)
    iterate_nested_list(nested_list, sub_list)
    print(nested_list)


def prob4(prob_num, keys, value):
    print(TAG, prob_num)
    res_dict = {}
    for i in range(len(keys)):
        res_dict[keys[i]] = value[i]
    print(res_dict)


def prob5(prob_num, dict1, dict2):
    print(TAG, prob_num)
    dict1.update(dict2)
    print(dict1)


def prob6(prob_num, sample_dict, old_key, new_key):
    print(TAG, prob_num)
    print("Initial dictionary:", sample_dict)
    sample_dict[new_key] = sample_dict.pop(old_key)
    print("Updated dictionary:", sample_dict)


def prob7(prob_num, dict_org):
    print(TAG, prob_num)
    res_list = []
    for keys, value in dict_org.items():
        res_list.append([keys, value])
    print(res_list)


prob1(1, [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]])
print()
prob2(2, ["Hello ", "take "], ["Dear", "sir"])
print()
prob3(3, ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"], ["h", "i", "j"])
print()
prob4(4, ["Ten", "Twenty", "Thirty"], [10, 20, 30])
print()
prob5(5, {'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {'Thirty': 30, 'Fourty': 40, 'Fifty': 50})
print()
prob6(6, {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}, "city", "location")
print()
prob7(7, {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]})
