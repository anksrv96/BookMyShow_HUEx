import csv

from GenericPages import GenericPages


class GenericFunctionalities:
    def perform_login(self):
        user_name = input('User: ')
        password = input('Password: ')
        role = self.perform_authentication_and_get_role(user_name, password)
        return role

    def perform_authentication_and_get_role(self, user_name, password):
        with open('AppData.csv', 'r') as infile:
            reader = csv.reader(infile, delimiter=',')
            next(reader)
            for row in reader:
                if row[0] == user_name:
                    if row[1] == password:
                        print('User Verified')
                        print('Logged in as ', row[2])
                        return row[2]
                        break
                    else:
                        print('Invalid Password')
                        break
                else:
                    continue
            print('Invalid credentials....Please try again ! ! !')
            self.perform_login()

    def perform_admin_action(self):
        try:
            admin_choice = int(input('Enter...'))
        except ValueError as ve:
            print("Invalid Choice....Please try again ! ! !")
            GenericPages.display_admin_home()
        except Exception as e:
            print("Something went wrong....Please try again ! ! !")
            GenericPages.display_admin_home()
        if admin_choice in [1, 2, 3, 4]:
            self.choose_valid_admin_action(admin_choice)
        else:
            print(print("Invalid Choice....Please try again ! ! !"))
            GenericPages.display_admin_home()

    def choose_valid_admin_action(self, admin_choice):
        match admin_choice:
            case 1:
                GenericPages.display_add_new_movie_page()
            case 2:
                GenericPages.display_edit_movie_page()
            case 3:
                GenericPages.display_delete_movie_page()
            case 4:
                GenericPages.display_home_screen()

