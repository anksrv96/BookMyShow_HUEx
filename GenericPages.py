import csv
import datetime


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

    @staticmethod
    def display_login_screen():
        print('******Welcome to BookMyShow*******')

    @staticmethod
    def display_register_new_user_page():
        print('****Create New Account****')

    @staticmethod
    def display_admin_home():
        print('******Welcome Admin*******')
        print('1. Add new movie info')
        print('2. Edit movie info')
        print('3. Delete movies')
        print('4. Logout')

    # displays user home and returns the number of valid responses
    @staticmethod
    def display_user_home():
        print('******Welcome User*******')
        counter = 0
        with open('movies.csv', 'r') as infile:
            reader = csv.reader(infile, delimiter=',')
            headers = next(reader)

            for row in reader:
                print(counter + 1, '. ', row[0])
                counter = counter + 1
        infile.close()
        print('0. Logout')
        return counter

    @staticmethod
    def display_add_new_movie_page():
        print('******Welcome Admin*******')

    # displays edt movie page and returns the number of valid responses
    @staticmethod
    def display_edit_movie_page():
        print('******Welcome Admin*******')
        print('Select the movie that you want to edit...')
        with open('movies.csv', 'r') as infile:
            reader = csv.reader(infile, delimiter=',')
            headers = next(reader)
            counter = 0
            for row in reader:
                print(counter + 1, '. ', row[0])
                print(dict(zip(headers, row)))
                counter = counter + 1
        infile.close()
        print('0. Main menu')
        return counter

    @staticmethod
    def display_delete_movie_page():
        print('******Welcome Admin*******')

    @staticmethod
    def display_user_actions():
        print('1. Book Tickets')
        print('2. Cancel Tickets')
        print('3. Give User Rating')

    def time_plus(self, time, timedelta):
        start = datetime.datetime(
            2000, 1, 1,
            hour=time.hour, minute=time.minute, second=time.second)
        end = start + timedelta
        return end.time()

    def display_book_ticket_screen(self, response):
        print('******Welcome User*******')
        print('Timings :')
        first_show = ''
        movie_length = ''
        no_of_shows = ''
        interval_time = ''
        gap = ''
        with open('movies.csv', 'r') as infile:
            reader = csv.reader(infile, delimiter=',')
            count = 0
            for row in reader:
                if count == response:
                    first_show = row[9]
                    movie_length = row[2]
                    no_of_shows = row[5]
                    interval_time = row[10]
                    gap = row[11]
                count = count + 1
        infile.close()
        timeobj = datetime.datetime(100, 1, 1, int(first_show[0:1]), int(first_show[-4:-2]), 0)
        time_delta = (int(movie_length) * 60) + int(interval_time) + int(gap)

        for i in range(int(no_of_shows)):
            print(i + 1, '. ', timeobj.strftime("%I:%M %p"))
            timeobj = timeobj + datetime.timedelta(minutes=time_delta)

    def display_cancel_ticket_screen(self, response):
        pass

    def display_user_rating_screen(self, response):
        print('Yet to programme this branch')
