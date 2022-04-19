import csv


class GenericPages:

    # Displays home screen and returns user input
    def display_home_screen(self):
        print('******Welcome to BookMyShow*******')
        print('1. Login')
        print('2. Register new account')
        print('3. Exit')
        try:
            user_choice = int(input('Enter...'))
        except ValueError as ve:
            print("Invalid Choice....Please try again ! ! !")
            self.display_home_screen()
        except Exception as e:
            print("Something went wrong....Please try again ! ! !")
            self.display_home_screen()
        if user_choice in [1, 2, 3]:
            return user_choice
        else:
            print(print("Invalid Choice....Please try again ! ! !"))
            self.display_home_screen()

    def display_login_screen(self):
        print('******Welcome to BookMyShow*******')

    def display_register_new_user_page(self):
        pass

    def display_admin_home(self):
        print('******Welcome Admin*******')
        print('1. Add new movie info')
        print('2. Edit movie info')
        print('3. Delete movies')
        print('4. Logout')



    def display_user_home(self):
        pass

    def display_add_new_movie_page(self):
        print('******Welcome Admin*******')

    def display_edit_movie_page(self):
        print('******Welcome Admin*******')
        print('Select the movie that you want to edit...')
        with open('movies.csv', 'r') as infile:
            reader = csv.reader(infile, delimiter=',')
            headers = next(reader)
            counter = 0
            for row in reader:
                print(counter+1, '. ', row[0])
                print(dict(zip(headers, row)))
                counter = counter+1
        infile.close()
        print('0. Main menu')
        return counter

    def display_delete_movie_page(self):
        print('******Welcome Admin*******')

