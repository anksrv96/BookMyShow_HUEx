import GenericFunctionalities


class GenericPages:
    gf = GenericFunctionalities.GenericFunctionalities()

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
        role = self.gf.perform_login()
        match role:
            case 'admin':
                self.display_admin_home()
            case 'user':
                self.display_user_home()

    def display_register_new_user_page(self):
        pass

    def display_admin_home(self):
        print('******Welcome Admin*******')
        print('1. Add new movie info')
        print('2. Edit movie info')
        print('3. Delete movies')
        print('4. Logout')
        self.gf.perform_admin_action()


    def display_user_home(self):
        pass
