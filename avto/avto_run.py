from avto_crud import menu
from avto_colorama import print_red
from avto_service import add_avto_query,update_avto_query,delete_avto_query,show_all_avto,get_avto_query


def run():
    while True:
        choice = menu()

        if choice == "1":
            show_all_avto()

        elif choice =="2":
            add_avto_query()

        elif choice == "3":
            delete_avto_query()

        elif choice == "4":
            update_avto_query()

        elif choice == "5":
            get_avto_query()

        elif choice == "6":
            break

        else:
            print_red("Wrong choice")




run()