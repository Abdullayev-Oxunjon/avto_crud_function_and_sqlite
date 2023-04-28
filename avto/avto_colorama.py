from colorama import Fore

def print_red(message):
    print(Fore.RED + message + Fore.RESET)

def print_yellow(message):
    print(Fore.YELLOW + message + Fore.RESET)

def print_saccess(message):
    print(Fore.MAGENTA + message + Fore.RESET)

def print_cyan(message):
    print(Fore.CYAN + message + Fore.RESET)