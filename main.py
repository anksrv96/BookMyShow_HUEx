from GenericPages import GenericPages

gp = GenericPages()


def main():
    user_choice = gp.display_home_screen()
    match user_choice:
        case 1:
            gp.display_login_screen()
        case 2:
            gp.display_register_new_user_page()




main()
