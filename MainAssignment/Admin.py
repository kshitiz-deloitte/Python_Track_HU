import re
from time import sleep

from Utils.ExcelReaderAndWriter import ExcelHelper
from Utils.readCfg import get_from_config


class Admin:
    __SECTION = "admin"
    __COM_SECTION = "common_attribute"
    __EXL_SECTION = "excel_file"
    admin_heading = ""

    def __init__(self):
        self.movies_dict = {}
        self.movies_header = []
        self.movies_data = ExcelHelper(get_from_config(self.__EXL_SECTION, "movies_sheet"))
        self.movies_header = self.movies_data.get_headers_from_exl()
        print("******Welcome to BookMyShow Admin*******")
        print(get_from_config(self.__SECTION, "admin_login_options"))
        ch = int(input(get_from_config(self.__COM_SECTION, "enter_option")))
        if ch == 1:
            self.admin_login()
        elif ch == 2:
            return

    def admin_login(self):
        print("******Welcome to BookMyShow Admin Login*******")
        admin_name = get_from_config(self.__SECTION, "admin_name")
        admin_password = get_from_config(self.__SECTION, "admin_pwd")
        admin_name_in = str(input("Admin Name: "))
        admin_password_in = str(input("Admin password: "))
        if admin_name == admin_name_in and admin_password_in == admin_password:
            self.admin_heading = f"******Welcome {admin_name}*******"
            self.admin_page()

    def admin_page(self):
        flag = True
        while flag:
            print(self.admin_heading)
            print(get_from_config(self.__SECTION, "admin_options"))
            ch = int(input(get_from_config(self.__COM_SECTION, "enter_option")))
            if ch == 1:
                print("******Add movie******")
                for header in self.movies_header:
                    if header == "Timings":
                        timing_str = ""
                        for elem in self.cal_movie_timing():
                            timing_str = " ".join([timing_str, str(elem)])
                        self.movies_dict[header] = timing_str.lstrip()

                        continue
                    self.movies_dict[header] = input(header + ": ")
                print(self.movies_dict)
                self.movies_data.insert_data_into_excel(list(self.movies_dict.items()))

            elif ch == 2:
                print("Edit movie details")
                count = 1
                movie_list = list(self.movies_data.get_data_from_exl())
                for movie in movie_list:
                    print(f"{count}. {movie[0]}")
                    count += 1
                movie_to_edit = movie_list[int(input("Enter the movie title to edit: "))-1][0]
                field_to_edit = input("Enter the field to edit: ")
                updated_value = input("Enter value to update: ")
                self.movies_data.edit_movie_from_excel(movie_to_edit, field_to_edit, updated_value)
            elif ch == 3:
                movie_to_delete = input("Enter the movie title to delete: ")
                if self.movies_data.del_movie_from_excel(movie_to_delete):
                    print("Movie deleted successfully")
                else:
                    print("Movie doesn't exist")
            elif ch == 4:
                print("Logging out...")
                self.movies_data.close_app()
                sleep(3)
                flag = False

    def get_hr_and_min(self, given_time):
        given_time = given_time.split(" ")
        cal_hr,cal_min = int(re.findall(r'\d+', given_time[0])[0]), int(re.findall(r'\d+', given_time[1])[0])

        return cal_hr, cal_min

    def cal_movie_timing(self):
        movie_length_hr, movie_length_min = self.get_hr_and_min(self.movies_dict["Length"])
        movie_number = int(self.movies_dict["Number of Shows in a day"])
        movie_first_show_hr, movie_first_show_min = self.get_hr_and_min(self.movies_dict["First show"])
        movie_interval_hr, movie_interval_min = self.get_hr_and_min(self.movies_dict["Interval Time"])
        movie_gap_hr, movie_gap_min = self.get_hr_and_min(self.movies_dict["Gap Between Shows"])
        total_run_time_min = movie_length_min + movie_interval_min
        min_to_hr = total_run_time_min // 60
        remaining_min = total_run_time_min % 60
        total_hr = movie_length_hr + movie_interval_hr + min_to_hr

        start_hr = 0
        start_min = 0
        for i in range(movie_number):
            if i == 0:
                start_hr = movie_first_show_hr
                start_min = movie_first_show_min
            end_min = remaining_min + start_min
            end_min_to_hr = end_min // 60
            end_remaining_min = end_min % 60
            end_hr = start_hr + end_min_to_hr + total_hr
            yield f"{start_hr}:{start_min}-{end_hr}:{end_remaining_min}"
            next_min = end_remaining_min + movie_gap_min
            next_min_to_hr = next_min // 60
            next_remaining_min = next_min % 60
            start_hr = end_hr + movie_gap_hr + next_min_to_hr
            start_min = next_remaining_min

admin = Admin()
admin.admin_page()