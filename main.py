import sys

from GenericFunctionalities import GenericFunctionalities
from GenericPages import GenericPages

gp = GenericPages()
gf = GenericFunctionalities()


# process flow if logged in as an ADMIN
def perform_appropriate_admin_action(admin_choice):
    match admin_choice:
        case 1:
            gp.display_add_new_movie_page()
            gf.add_new_movie()
            gp.display_admin_home()
            admin_choice = gf.register_admin_choice()
            perform_appropriate_admin_action(admin_choice)
        case 2:
            acceptable_response_range = gp.display_edit_movie_page()
            # print('Total movies found...', acceptable_response_range)
            response = gf.register_response_for_movie_list_editing(acceptable_response_range)
            if response == 0:
                gp.display_admin_home()
                admin_choice = gf.register_admin_choice()
                perform_appropriate_admin_action(admin_choice)
            else:
                gf.edit_selected_movie(response)
                gp.display_admin_home()
                admin_choice = gf.register_admin_choice()
                perform_appropriate_admin_action(admin_choice)
        case 3:
            gp.display_delete_movie_page()
            gf.register_admin_choice_and_delete_movie()
            gp.display_admin_home()
            admin_choice = gf.register_admin_choice()
            perform_appropriate_admin_action(admin_choice)

        case 4:
            main()


# process flow if logged in as a USER
def perform_appropriate_user_action(response):
    tickets_remaining = gf.fetch_and_display_movie_details(response)
    gp.display_user_actions()
    user_choice = gf.register_user_response_for_action_selection()
    match user_choice:
        case 1:
            gp.display_book_ticket_screen(response)
            gf.perform_ticket_sale(response)
            main()
        case 2:
            gp.display_cancel_ticket_screen(response)
        case 3:
            gp.display_user_rating_screen(response)


def main():
    user_choice = gp.display_home_screen()
    user_role = ""
    match user_choice:
        case 1:
            gp.display_login_screen()
            user_role = gf.perform_login()
            if user_role == 'admin':
                gp.display_admin_home()
                admin_choice = gf.register_admin_choice()
                perform_appropriate_admin_action(admin_choice)
            elif user_role == 'user':
                acceptable_response_range = gp.display_user_home()
                response = gf.register_user_response_for_movie_selection(acceptable_response_range)
                if response == 0:
                    main()
                else:
                    perform_appropriate_user_action(response)

        case 2:
            gp.display_register_new_user_page()
            gf.register_new_user()
            main()
        case 3:
            sys.exit("Terminating ! ! !")


main()
