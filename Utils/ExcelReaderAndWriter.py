import openpyxl
import xlwings as xw
# Give the location of the file
from Utils.readCfg import get_from_config



class ExcelHelper:
    __headers = []
    ASCII_VALUE = 96

    def __init__(self, sheet_name):
        self.app = xw.App(add_book=False)
        self.wb = self.app.books.open(get_from_config("excel_file", "file_path"))
        self.my_sheet_obj = self.wb.sheets[sheet_name]

    def get_row_column(self):
        return self.my_sheet_obj.range('A' + str(self.my_sheet_obj.cells.last_cell.row)).end('up').row, self.my_sheet_obj.range('A1').end('right').column


    def get_headers_from_exl(self):
        row, col = self.get_row_column()
        self.__headers = self.my_sheet_obj.range(f"{chr(self.ASCII_VALUE+1)}1:{chr(self.ASCII_VALUE+col)}1").value
        return self.__headers

    def get_headers(self):
        return self.__headers

    def get_data_from_exl(self):
        row, col = self.get_row_column()
        for i in range(1, row):
            yield self.my_sheet_obj.range(f"{chr(self.ASCII_VALUE + 1)}{i+1}:{chr(self.ASCII_VALUE + col)}{i+1}").value


    def insert_data_into_excel(self, input_data):
        row, col = self.get_row_column()
        print(col)
        count = 1
        for data in input_data:
            self.my_sheet_obj.range(f"{chr(self.ASCII_VALUE + count)}{row+1}").value = data
            count += 1

        try:
            self.wb.save()
            self.wb.save(get_from_config("excel_file", "file_path"))
        except Exception as e:
            print(e)

    def del_movie_from_excel(self, movie_to_delete):
        row, col = self.get_row_column()
        delete_movie_row = 0
        flag = False
        for movie in self.my_sheet_obj.range('A2:A{}'.format(row)):
            if movie_to_delete == movie.value:
                print(movie.value)
                delete_movie_row = int(movie.get_address(0, 0)[1:])
                print(delete_movie_row)
                self.my_sheet_obj.range('2:{}'.format(delete_movie_row)).api.Delete()
                break
        if delete_movie_row != 0:
            flag = True
            try:
                self.wb.save()
                self.wb.save(get_from_config("excel_file", "file_path"))
            except Exception as e:
                print(e)
        return flag


    def edit_movie_from_excel(self, movie_to_edit, field_to_edit, updated_value):
        row, col = self.get_row_column()
        edit_movie_row = 0
        edit_movie_col = 0
        for movie in self.my_sheet_obj.range('A2:A{}'.format(row)):
            if movie_to_edit == movie.value:
                edit_movie_row = int(movie.get_address(0, 0)[1:])
                for header in self.__headers:
                    if header == field_to_edit:
                        print(header)
                        edit_movie_col = int(self.__headers.index(field_to_edit))
        print(edit_movie_col, edit_movie_row)
        print(f"{chr(self.ASCII_VALUE + edit_movie_col + 1)}{edit_movie_row + 1}")
        self.my_sheet_obj.range(f"{chr(self.ASCII_VALUE + edit_movie_col + 1)}{edit_movie_row}").value = updated_value
        try:
            self.wb.save()
            self.wb.save(get_from_config("excel_file", "file_path"))
        except Exception as e:
            print(e)

    def close_app(self):
        self.app.quit()






# movies_data = ExcelHelper(get_from_config("excel_file", "movies_sheet"))
# # # movies_data.get_headers_from_exl()
# # # print(list(movies_data.get_data_from_exl()))
# movies_data.insert_data_into_excel(['Test3', 'Fantasy', '2hr 30m', 'Robert Jr.', 'Stan lee', 3.5, 'Eng', "4", "8h 0m", '0h 30m', '0h 15min', "1-2 2-3", 2.0])
# movies_data.close_app()
# movies_data.del_movie_from_excel("Test")