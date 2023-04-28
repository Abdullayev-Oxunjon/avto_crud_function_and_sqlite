# from uuid import UUID, uuid4
# from colorama import Fore
#
#
# def print_successfully(message):
#     print(Fore.RED + message + Fore.RESET)
#
#
# class Book:
#
#     def __init__(self, title, description, author, price, created_at):
#         self.title = title
#         self.description = description
#         self.author = author
#         self.price = price
#         self.created_at = created_at
#         self.id = uuid4()
#
#     def __str__(self):
#         return f"""Id: {self.id}
#                    Title: {self.title}
#                    Description: {self.description}
#                    Author: {self.author}
#                    Price: {self.price}
#                    Data: {self.created_at}"""
#
#
# class BookRun:
#
#     def __init__(self):
#         self.book_list = []
#         book = Book(title="Ufq",
#              description="Trellogiya",
#              author="Said Ahmad",
#              price=50_000,
#              created_at="02-05-2010")
#         self.book_list.append(book)
#
#     def menu(self):
#         print("Book list => 1")
#         print("Add Book => 2")
#         print("Delete Book => 3")
#         print("Update Book => 4")
#         print("Quit => 5")
#         return input("=> ")
#
#     def show_all(self):
#         for index, book in enumerate(self.book_list, start=1):
#             print(f"{index}. {book}")
#
#     def add_book(self):
#         title = input("Title : ")
#         description = input("Description : ")
#         author = input("Author : ")
#         price = input("Price : ")
#         data = input("Data : ")
#         book = Book(title=title,
#              description=description,
#              author=author,
#              price=price,
#              created_at=data)
#         self.book_list.append(book)
#
#     def update_book(self):
#         self.show_all()
#         choice = int(input(" => "))
#         if choice < 0 and choice > len(self.book_list):
#             print("Wrong choice")
#
#         title = input("Title : ")
#         description = input("Description : ")
#         author = input("Author : ")
#         price = int(input("Price : "))
#         data = input("Data : ")
#
#         book = self.book_list[choice-1]
#         if len(title) > 0:
#             book.title = title
#         if len(description) > 0:
#             book.description = description
#         if len(author) > 0:
#             book.author = author
#         if price > 0:
#             book.price = price
#         if len(data) > 0:
#             book.created_at = data
#
#     def delete_book(self):
#         self.show_all()
#         choice = int(input(" => "))
#         if choice < 0 and choice > len(self.book_list):
#             print("Wrong choice")
#         else:
#             del self.book_list[choice - 1]
#
#     def run(self):
#         while True:
#             choice = self.menu()
#             if choice == "1":
#                 self.show_all()
#             elif choice == "2":
#                 self.add_book()
#             elif choice == "3":
#                 self.delete_book()
#             elif choice == "4":
#                 self.update_book()
#             elif choice == "5":
#                 break
#             else:
#                 # print(Fore.RED + "Wrong choice" + Fore.RESET)
#                 print_successfully("Wrong choice")
#
#
# book_run = BookRun()
# print(book_run.run())


from uuid import uuid4
from colorama import Fore
from avto_colorama import print_yellow,print_red
from avto_init import Avto









