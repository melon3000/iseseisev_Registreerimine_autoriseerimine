from ast import Str
import os
import random
from os import system
from time import sleep

YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = '\033[31m'
G = '\033[90m'
R = "\033[0m"

#----------------------------------------------------------------------------------
def title():
    """Aken pealkirja animatsioon.
    Kuvab "github.com/melon3000" tähemärkide kaupa akna pealkirjana.
    """
    system('cls')
    text = ''
    for char in "github.com/melon3000":
        text += char
        system(f'title {text}')
        sleep(0.01)
    system('title github.com/melon3000')

#----------------------------------------------------------------------------------
def get_user(user_login_status: bool, login: str = '') -> str:
    """Tagastab aktiivse kasutaja nime."""
    if user_login_status == 0:
        return os.getenv("USERNAME")
    elif user_login_status == 1:
        return login

#----------------------------------------------------------------------------------
def menu(current_user: str) -> int:
    """Kuvab valikumenüü ja tagastab kasutaja valiku."""
    while True:
        try:
            system('cls')
            print(f"""{G}Logitud kui: {GREEN}{current_user}{G}\n
┌[{GREEN}1{G}] - Registreerimine
├[{GREEN}2{G}] - Autoriseerimine
├[{GREEN}3{G}] - Nime või parooli muutmine
├[{GREEN}4{G}] - Unustanud parooli taastamine
└[{GREEN}5{G}] - Lõpetamine
""")
            func_choice = int(input("> "))
            if 1 <= func_choice <= 5:
                return func_choice
            else:
                print(f"{RED}Sisetage ainult numbrid 1-5!{R}")
                sleep(1)
        except ValueError:
            print(f"{RED}Sisetage ainult numbrid 1-5!{R}")
            sleep(1)

#----------------------------------------------------------------------------------
def checkpassword(password: str) -> bool:
    """Kontrollib, kas parool vastab turvanõuetele."""
    symbols1 = list(".,:;!_*-+()/#¤%&")
    symbols2 = list("0123456789")
    symbols3 = list('qwertyuiopasdfghjklzxcvbnm')
    symbols4 = list('QWERTYUIOPASDFGHJKLZXCVBNM')

    has_symbols = has_digits = has_lowercase = has_uppercase = False

    for char in password:
        if char in symbols1:
            has_symbols = True
        if char in symbols2:
            has_digits = True
        if char in symbols3:
            has_lowercase = True
        if char in symbols4:
            has_uppercase = True
        
        if has_symbols and has_digits and has_lowercase and has_uppercase:
            print(f'{GREEN}Parool vastab normile{R}.')
            sleep(3)
            return True
    print(f'{RED}Parool ei vasta normile!{R}')
    sleep(3)
    return False

#----------------------------------------------------------------------------------
def generatePassword() -> str:
    """Genereerib juhusliku turvalise parooli."""
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    return ''.join([random.choice(ls) for i in range(12)])

#----------------------------------------------------------------------------------
def register(users: dict):
    """Registreerib uue kasutaja."""
    system('cls')
    username = input(f"{G}Sisesta nimi: {R}")
    
    if username.lower() in (name.lower() for name in users):
        print(f"{RED}Viga! Nimi on juba kasutusel.{R}")
        sleep(3)
        return 
    
    password_method_choice = int(input(f"{GREEN}1 {G}- Autogenereerimine, {GREEN}2 {G}- Manuaalne: {R}{GREEN}"))
    print(f'{R}')    

    if password_method_choice == 1:
        users[username] = generatePassword()
        print(f"{G}Kasutaja {GREEN}{username}{G} on registreeritud!")
        print(f"{R}Teie parool:{GREEN}{users[username]}{G}")
        system('echo. & echo Vajuta mõni nupp... & pause >nul')
        
    elif password_method_choice == 2:
        password = input("Sisesta parool: ")
        if checkpassword(password):
            users[username] = password
            print(f"{G}Kasutaja {GREEN}{username}{G} on registreeritud!")
    sleep(3)

#----------------------------------------------------------------------------------
def auth(username: str, password: str, users: dict):
    """Kontrollib, kas kasutaja ja parool on õiged."""
    system('cls')

    if username.lower() in (name.lower() for name in users):
        if users[username.lower()] == password:
            print(f"Õnnitlused, {GREEN}{username}{R}! Olete edukalt sisse logitud.")
            sleep(3)
            return username, 1
        else:
            print(f"{RED}Vale parool!{R}")
            sleep(3)
    else:
        print(f"{RED}Pole kasutajat seda nimega.{R}")
        sleep(3)
    return None, 0

#----------------------------------------------------------------------------------
def change_credentials(users: dict, username: str, login: str, user_login_status: bool):
    """Võimaldab kasutajal muuta oma nime või parooli, kui ta on sisse logitud ja tema login vastab sisestatud kasutajale.
    
    :param dict users: kasutajate andmebaas
    :param str username: aktiivne kasutajanimi
    :param str login: sisse logitud kasutaja nimi
    :param bool user_login_status: kas kasutaja on sisse logitud (1) või mitte (0)
    """
    system('cls')

    # Kontrollime, kas kasutaja on sisse logitud ja kas login vastab username-le
    if user_login_status == 0 or username != login:
        print(f"{RED}Viga! Peate olema sisse logitud ja kasutama oma andmeid.{R}")
        sleep(3)
        return
    
    print(f"""{G}Mida soovite muuta?
┌[{GREEN}1{G}] - Muuda kasutajanime
└[{GREEN}2{G}] - Muuda parooli
""")
    choice = input("> ")
    
    if choice == "1":
        new_username = input(f"{G}Sisesta uus kasutajanimi: {R}")
        if new_username in users:
            print(f"{RED}Viga! See nimi on juba kasutusel.{R}")
            sleep(3)
            return
        users[new_username] = users.pop(username)
        print(f"{GREEN}Kasutajanimi muudetud! Uus nimi: {new_username}{R}")
    
    elif choice == "2":
        new_password = input(f"{G}Sisesta uus parool: {R}")
        if checkpassword(new_password):
            users[username] = new_password
            print(f"{GREEN}Parool edukalt muudetud!{R}")
    
    else:
        print(f"{RED}Vale valik!{R}")
    
    sleep(3)

#----------------------------------------------------------------------------------
def restorePassword(user_login_status: bool, login:str, username: str, users: dict):
    """Laseb kasutajal parooli lähtestada."""

    if user_login_status == 0 or username != login:
        print(f"{RED}Viga! Peate olema sisse logitud ja kasutama oma andmeid.{R}")
        sleep(2)
        return

    if username in users and username == login:
        new_password = generatePassword()
        users[username] = new_password
        print(f"{GREEN}Uus parool kasutajale {username}: {new_password}{R}")
    else:
        print(f"{RED}Kasutajat ei leitud!{R}")
    sleep(2)