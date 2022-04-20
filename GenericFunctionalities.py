import csv


class GenericFunctionalities:
    def perform_login(self):
        user_name = input('User: ')
        password = input('Password: ')
        role = self.perform_authentication_and_get_role(user_name, password)
        return role

    def perform_authentication_and_get_role(self, user_name, password):
        with open('credentials.csv', 'r') as infile:
            reader = csv.reader(infile, delimiter=',')
            next(reader)
            for row in reader:
                if row[0] == user_name:
                    if row[1] == password:
                        print('User Verified')
                        print('Logged in as ', row[2])
                        return row[2]
                    else:
                        print('Invalid Password')
                        break
                else:
                    continue
            print('Invalid credentials....Please try again ! ! !')
            self.perform_login()

    def register_admin_choice(self):
        try:
            admin_choice = int(input('Enter...'))
        except ValueError as ve:
            print("Invalid Choice....Please try again ! ! !")
            self.register_admin_choice()
        except Exception as e:
            print("Something went wrong....Please try again ! ! !")
            self.register_admin_choice()
        if admin_choice in [1, 2, 3, 4]:
            return admin_choice
        else:
            print(print("Invalid Choice....Please try again ! ! !"))
            self.register_admin_choice()

    def add_new_movie(self):
        # taking user inputs for movie
        movie_details = []
        movie_details.append(input('Title: '))
        movie_details.append(input('Genre: '))
        movie_details.append(input('Length(in hours) : '))
        movie_details.append(input('Cast: '))
        movie_details.append(input('Director: '))
        movie_details.append(input('Admin Ratings: '))
        movie_details.append(input('Language: '))
        movie_details.append(input('Timings(not mandatory): '))
        movie_details.append(input('Number of shows in a day: '))
        movie_details.append(input('First show(like hh.mmAM): '))
        movie_details.append(input('Interval Time(in mins): '))
        movie_details.append(input('Gap between shows(in mins): '))
        movie_details.append(input('Capacity: '))

        # writing to csv
        with open('movies.csv', 'a', newline='') as infile:
            writer = csv.writer(infile)
            writer.writerow(movie_details)
        infile.close()

        print(movie_details[0], ' was successfully added to the movie list')

    def register_response_for_movie_list_editing(self, valid_range):
        try:
            admin_choice_to_edit_movie = int(input('Enter...'))
        except ValueError as ve:
            print("Invalid Choice....Please try again ! ! !")
            self.register_response_for_movie_list_editing(valid_range)
        except Exception as e:
            print("Something went wrong....Please try again ! ! !")
            self.register_response_for_movie_list_editing(valid_range)

        if admin_choice_to_edit_movie in range(0, valid_range + 1):
            return admin_choice_to_edit_movie
        else:
            print(print("Invalid Choice....Please try again ! ! !"))
            self.register_response_for_movie_list_editing(valid_range)

    def edit_selected_movie(self, response):
        print('Making changes')
        new_movie_list = []
        updated_movie_details = self.get_updated_movie_details()
        with open('movies.csv', 'r') as infile:
            reader = csv.reader(infile, delimiter=',')
            counter = 0
            for row in reader:
                print(row)
                if counter == response:
                    new_movie_list.append(updated_movie_details)
                else:
                    new_movie_list.append(row)
                counter = counter + 1
        infile.close()

        print(new_movie_list)

        with open('movies.csv', 'w+', newline='') as infile:
            writer = csv.writer(infile)
            writer.writerows(new_movie_list)
        infile.close()

    def get_updated_movie_details(self):
        movie_details = []
        movie_details.append(input('Title: '))
        movie_details.append(input('Genre: '))
        movie_details.append(input('Length: '))
        movie_details.append(input('Cast: '))
        movie_details.append(input('Director: '))
        movie_details.append(input('Admin Ratings: '))
        movie_details.append(input('Language: '))
        movie_details.append(input('Timings: '))
        movie_details.append(input('Number of shows in a day: '))
        movie_details.append(input('First show: '))
        movie_details.append(input('Interval Time: '))
        movie_details.append(input('Gap between shows: '))
        movie_details.append(input('Capacity: '))

        return movie_details

    def register_admin_choice_and_delete_movie(self):
        try:
            movie_to_be_deleted = input('Enter movie title that needs to be deleted...')
        except Exception as e:
            print('Something went wrong. Try again')
            self.register_admin_choice_and_delete_movie()

        new_movie_list = []

        with open('movies.csv', 'r') as infile:
            reader = csv.reader(infile, delimiter=',')
            for row in reader:
                if row[0] == movie_to_be_deleted:
                    continue
                else:
                    new_movie_list.append(row)
        infile.close()

        with open('movies.csv', 'w+', newline='') as infile:
            writer = csv.writer(infile)
            writer.writerows(new_movie_list)
        infile.close()

    def register_user_response_for_movie_selection(self, valid_range):
        user_response_for_movie_selection = 0
        try:
            user_response_for_movie_selection = int(input('Enter...'))
        except ValueError as ve:
            print("Invalid Choice....Please try again ! ! !")
            self.register_user_response_for_movie_selection(valid_range)
        except Exception as e:
            print("Something went wrong....Please try again ! ! !")
            self.register_user_response_for_movie_selection(valid_range)
        if user_response_for_movie_selection in range(0, valid_range + 1):
            return user_response_for_movie_selection
        else:
            print(print("Invalid Choice....Please try again ! ! !"))
            self.register_user_response_for_movie_selection(valid_range)

    def fetch_and_display_movie_details(self, response):
        tickets_remaining = 0
        movie_details = []
        with open('movies.csv', 'r') as infile:
            reader = csv.reader(infile, delimiter=',')
            movie_attributes = ['Title:', 'Genre:', 'Length:', 'Cast:', 'Director:', 'Admin Rating:', 'Timings:']
            next(reader)
            count = 1

            for row in reader:
                if count == response:
                    movie_details.append(row[0])
                    movie_details.append(row[1])
                    movie_details.append(row[2])
                    movie_details.append(row[3])
                    movie_details.append(row[4])
                    movie_details.append(row[5])
                    movie_details.append(row[7])
                    tickets_remaining = row[12]
                count = count + 1
        infile.close()

        for i in range(len(movie_attributes) - 1):
            print(movie_attributes[i], movie_details[i])

        return tickets_remaining

    def register_user_response_for_action_selection(self):
        user_response = 0
        try:
            user_response = int(input('Enter...'))
        except ValueError as ve:
            print('Invalid Input...Try Again')
            self.register_user_response_for_action_selection()
        except Exception as e:
            print('Something went wrong...Try Again')
            self.register_user_response_for_action_selection()

        if user_response in [1, 2, 3]:
            return user_response
        else:
            print('Invalid Input...Try Again')
            self.register_user_response_for_action_selection()

    def register_new_user(self):
        new_user_data = []
        new_user_data.append(input("Name: "))
        new_user_data.append(input("Password: "))
        new_user_data.append('user')
        new_user_data.append(input("Email: "))
        new_user_data.append(input("Phone: "))
        new_user_data.append(input("Age: "))
        with open('credentials.csv', 'a+', newline='') as infile:
            writer = csv.writer(infile)
            writer.writerow(new_user_data)
        infile.close()

    def perform_ticket_sale(self, response):
        movie_name = ''
        capacity = 0
        new_row = ['', '', '', '', '', '']
        try:
            slot_selection = int(input('Enter'))
        except Exception:
            print("Something went wrong. Try Again")
            self.perform_ticket_sale()

        with open('movies.csv', 'r') as infile:
            reader = csv.reader(infile, delimiter=',')
            counter = 0
            for row in reader:
                if counter == response:
                    movie_name = row[0]
                    capacity = int(row[12])
                counter = counter+1
        infile.close()

        print('Remaining seats are ... ', capacity)
        no_of_tickets = int(input('Enter number of seats to be booked ...'))

        new_row[0] = movie_name
        new_row[slot_selection] = int(capacity) - no_of_tickets

        if no_of_tickets >= capacity:
            print('Requested number of seats are NOT available....Please try again')
            self.perform_ticket_sale()
        else:
            print('Thanks for booking')
            with open('box_office.csv', 'a+', newline='') as infile:
                writer = csv.writer(infile)
                writer.writerow(new_row)






