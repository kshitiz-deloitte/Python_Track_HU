import openpyxl
import xlwings as xw
# Give the location of the file
from Utils.readCfg import get_from_config

app = xw.App(add_book=False)
wb = app.books.open(get_from_config("excel_file", "file_path"))


class ExcelHelper:
    __headers = []
    ASCII_VALUE = 96

    def __init__(self, sheet_name):
        self.my_sheet_obj = wb.sheets[sheet_name]

    def get_row_column(self):
        return self.my_sheet_obj.range('A1').end('down').row, self.my_sheet_obj.range('A1').end('right').column


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
        # for i in range(2, self.row + 1):
        #     for j in range(1, self.column + 1):
        #         print(self.my_sheet_obj.cell(row=i, column=j).value)

    def insert_data_into_excel(self, input_data):
        row, col = self.get_row_column()
        print(col)
        count = 1
        for data in input_data:
            print(data)
            print(f"{chr(self.ASCII_VALUE + count)}{row+1}")
            self.my_sheet_obj.range(f"{chr(self.ASCII_VALUE + count)}{row+1}").value = data
            count += 1
        wb.save()
        wb.save(get_from_config("excel_file", "file_path"))

    def del_movie_from_excel(self, movie_to_delete):
        row, col = self.get_row_column()
        delete_movie_row = 0
        for movie in self.my_sheet_obj.range('A2:A{}'.format(row)):
            if movie_to_delete == movie.value:
                delete_movie_row = int(movie.get_address(0, 0)[1:])
        self.my_sheet_obj.range('2:{}'.format(delete_movie_row)).api.Delete()
        wb.save()
        print(get_from_config("excel_file", "file_path"))
        wb.save(get_from_config("excel_file", "file_path"))




movies_data = ExcelHelper(get_from_config("excel_file", "movies_sheet"))
# movies_data.get_headers_from_exl()
# print(list(movies_data.get_data_from_exl()))
movies_data.insert_data_into_excel(['Avengers', 'Fantasy', '2hr 30m', 'Robert Jr.', 'Stan lee', 3.5, 'Eng', "4", "8h 0m", '0h 30m', '0h 15min', "1-2 2-3", 2.0])
# movies_data.del_movie_from_excel("Test")