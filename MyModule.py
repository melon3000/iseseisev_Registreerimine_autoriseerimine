import smtplib, ssl
from email.message import EmailMessage
import random
from time import sleep
import os
from os import system

YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = '\033[31m'
G = '\033[90m'
R = "\033[0m"

def load(filename="saves.txt"):
    usernames = []
    passwords = []
    emails = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts) == 3:
                username, password, email = parts
                usernames.append(username)
                passwords.append(password)
                emails.append(email)
    
    return usernames, passwords, emails

def save(usernames, passwords, emails, filename="saves.txt"):
    if not (len(usernames) == len(passwords) == len(emails)):
        raise ValueError("Списки usernames, passwords и emails должны быть одинаковой длины.")

    with open(filename, "w", encoding="utf-8") as file:
        for username, password, email in zip(usernames, passwords, emails):
            file.write(f"{username} | {password} | {email}\n")


#----------------------------------------------------------------------------------#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
#----------------------------------------------------------------------------------#
def send_mail(to_email: str, subject: str, body: str):
    """Функция для отправки письма на почту."""
    from_email = ""  # Замените на ваш адрес электронной почты
    from_password = ""  # Замените на ваш пароль от почты (лучше использовать App Password)
    
    # Формируем письмо
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    
    # Устанавливаем параметры для подключения к SMTP серверу через TLS
    context = ssl.create_default_context()

    try:
        # Подключаемся к SMTP серверу
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(from_email, from_password)
            server.send_message(msg)
            print(f"Письмо отправлено на {to_email}")
    except Exception as e:
        print(f"Ошибка при отправке письма: {str(e)}")

#----------------------------------------------------------------------------------
def title():
    """Aken pealkirja animatsioon."""
    system('cls')
    sleep(0.1)
    text = ''
    for char in "github.com/melon3000":
        text += char
        system(f'title {text}')
        sleep(0.03)
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
def register(usernames: list, passwords: list, emails: list):
    """Registreerib uue kasutaja koos e-posti aadressiga."""
    system('cls')
    username = input(f"{G}Sisesta nimi: {R}")
    
    if username.lower() in (name.lower() for name in usernames):
        print(f"{RED}Viga! Nimi on juba kasutusel.{R}")
        sleep(3)
        return 
    
    email = input(f"{G}Sisesta oma e-posti aadress: {R}")
    
    # Kontrollime, kas e-posti aadress on juba kasutusel
    if email.lower() in (mail.lower() for mail in emails):
        print(f"{RED}Viga! E-posti aadress on juba kasutusel.{R}")
        sleep(3)
        return
    
    password_method_choice = int(input(f"{GREEN}1 {G}- Autogenereerimine, {GREEN}2 {G}- Manuaalne: {R}{GREEN}"))
    print(f'{R}')    

    if password_method_choice == 1:
        generated_password = generatePassword()
        usernames.append(username)
        passwords.append(generated_password)
        emails.append(email)
        print(f"{G}Kasutaja {GREEN}{username}{G} on registreeritud!")
        print(f"{R}Teie parool:{GREEN}{generated_password}{G}")
        
        # Saadame e-kirja registreerimisest
        send_mail(email, "Tere tulemast!", f"Teie konto on edukalt loodud. Kasutajanimi: {username}, Parool: {generated_password}")
        
        system('echo. & echo Vajuta mõni nupp... & pause >nul')
        
    elif password_method_choice == 2:
        password = input("Sisesta parool: ")
        if checkpassword(password):
            usernames.append(username)
            passwords.append(password)
            emails.append(email)
            print(f"{G}Kasutaja {GREEN}{username}{G} on registreeritud!")
            
            # Saadame e-kirja registreerimisest
            send_mail(email, "Tere tulemast!", f"Teie konto on edukalt loodud. Kasutajanimi: {username}, Parool: {password}")
    
    save(usernames, passwords, emails)
    sleep(3)

#----------------------------------------------------------------------------------
def auth(username: str, password: str, usernames: list, passwords: list, emails: list):
    """Kontrollib, kas kasutaja ja parool on õiged."""
    system('cls')

    if username.lower() in (name.lower() for name in usernames):
        index = usernames.index(username.lower())
        if passwords[index] == password:
            print(f"Õnnitlused, {GREEN}{username}{R}! Olete edukalt sisse logitud.")
            
            # Saadame e-kirja logimisest
            send_mail(emails[index], "Logimine edukas", f"Tere, {username}! Olete edukalt sisse logitud.")
            
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
def change_credentials(usernames: list, passwords: list, username: str, login: str, user_login_status: bool, emails: list):
    """Võimaldab kasutajal muuta oma nime või parooli, kui ta on sisse logitud ja tema login vastab sisestatud kasutajale."""
    system('cls')

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
        if new_username in usernames:
            print(f"{RED}Viga! See nimi on juba kasutusel.{R}")
            sleep(3)
            return
        usernames[usernames.index(username)] = new_username
        print(f"{GREEN}Kasutajanimi muudetud! Uus nimi: {new_username}{R}")
        
        # Saadame e-kirja nime muutmisest
        index = usernames.index(new_username)
        send_mail(emails[index], "Kasutajanimi muudetud", f"Teie kasutajanimi on edukalt muudetud. Uus nimi: {new_username}")
    
    elif choice == "2":
        new_password = input(f"{G}Sisesta uus parool: {R}")
        if checkpassword(new_password):
            passwords[usernames.index(username)] = new_password
            print(f"{GREEN}Parool edukalt muudetud!{R}")
            
            # Saadame e-kirja parooli muutmisest
            index = usernames.index(username)
            send_mail(emails[index], "Parool muudetud", f"Teie parool on edukalt muudetud.")
    
    else:
        print(f"{RED}Vale valik!{R}")
    
    sleep(3)

#----------------------------------------------------------------------------------
def restorePassword(user_login_status: bool, login:str, username: str, usernames: list, passwords: list, emails: list):
    """Laseb kasutajal parooli lähtestada."""

    if user_login_status == 0 or username != login:
        print(f"{RED}Viga! Peate olema sisse logitud ja kasutama oma andmeid.{R}")
        sleep(2)
        return

    if username in usernames and username == login:
        new_password = generatePassword()
        passwords[usernames.index(username)] = new_password
        print(f"{GREEN}Uus parool kasutajale {username}: {new_password}{R}")
        
        # Saadame e-kirja parooli taastamisest
        index = usernames.index(username)
        send_mail(emails[index], "Parool taastatud", f"Teie parool on taastatud. Uus parool: {new_password}")
        
    else:
        print(f"{RED}Kasutajat ei leitud!{R}")
    sleep(2)

#----------------------------------------------------------------------------------

