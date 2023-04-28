from avto_init import Avto
from avto_colorama import print_yellow,print_red,print_cyan



avto_list = []

def menu():
    print_cyan("AVTO LIST --------------- 1")
    print_cyan("ADD AVTO --------------- 2")
    print_cyan("DELETE AVTO --------------- 3")
    print_cyan("UPDATE AVTO --------------- 4")
    print_cyan("GET AVTO  -------------- 5")
    print_yellow("QUIT  --------------- 6")
    return input("==>")

def show_all():
    for index , avto in enumerate(avto_list,start=1):
        print(f"{index}  {avto}")

def add_avto():

    make = input("Make : ")
    model = input("Model : ")
    color = input("Color : ")
    price = input("Price: ")
    avto = Avto(make = make,
                model = model,
                color = color,
                price = price)
    avto_list.append(avto)


def delete_avto():
    show_all()
    choice = int(input("Tanlang : "))

    if choice < 0 or choice > len(avto_list):
        print_red("Wrong choice")

    else:

        del avto_list[choice - 1]


def update_avto():

    show_all()
    choice = int(input(" --->"))

    if choice < 0 or choice > len(avto_list):
        print_red("Wrong choice")

    else:
        make = input("Make : ")
        model = input("Model : ")
        color = input("Color : ")
        price = input("Price: ")

        avto = avto_list[choice - 1]

        if len(make) > 0:
            avto.make = make

        if len(model) > 0:
            avto.model = model

        if len(color) > 0:
            avto.color = color

        if len(price) > 0:
            avto.price = price
        print_yellow("Saccesfully result")