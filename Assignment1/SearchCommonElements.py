from Assignment1.StringClass import StringClass


class SearchCommonElements(StringClass):

    def common_elements(self, object_next_class):
        self.convert_into_list_char()
        object_next_class.convert_into_list_char()
        print(self.get_char_list(), object_next_class.get_char_list())
