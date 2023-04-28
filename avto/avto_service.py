from avto_db import avtolar
from avto_db import add_avto,cursor,commit
from avto_colorama import print_red,print_yellow,print_saccess,print_cyan

@commit

def show_all_avto():

    for  avto in avtolar:
        print(f"   {avto}")


def get_avto_query():
    show_all_avto()
    get = int(input(" --->"))
    car = cursor.execute(f""" select * from avto where id = {get}""").fetchone()
    if not car:
        print_red("Wrong choice")
    else:
        print(car)


@commit
def add_avto_query():

    make = input("Make : ")
    model = input("model : ")
    color = input("color : ")
    price = input("  price: ")

    query_param = (make,model,color,price)
    cursor.execute(add_avto,query_param)



@commit
def update_avto_query():
    show_all_avto()
    id = int(input(" --->"))

    kurs = cursor.execute(f""" select * from course where id = {id}""").fetchone()

    if not kurs:
        print_red("Wrong choice")

    else:
        make = input("Make : ")
        model = input("model : ")
        color = input("color : ")
        price = input("  price: ")

        cursor.execute(f"""
        
        update avto set  make = '{make}',
         model = '{model}',
         color = '{color}',
         price = '{price}'
         where id = {id}
        
        
        """)
        print_cyan("Saccesfully update")


@commit
def delete_avto_query():

    show_all_avto()
    id = int(input(" --->"))

    car = cursor.execute(f""" select * from avto where id = {id}""").fetchone()

    if not car:
        print_red("Wrong choice")

    else:
        cursor.execute(f"""
        
        delete from avto where id = {id}
        
        """)
        print_yellow("Saccessfully delete")
