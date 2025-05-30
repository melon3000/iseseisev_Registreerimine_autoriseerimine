from MyModule import *

title()

user_login_status = 0
login = ''

usernames, passwords, emails = load()

while True:
    current_user = get_user(user_login_status, login)
    func_choice = menu(current_user)

    if func_choice == 1:
        print("Registreerimine valitud.")
        sleep(0.5)
        register(usernames, passwords, emails)

    elif func_choice == 2:
        print("Autoriseerimine valitud.")
        sleep(0.5)
        username = input(f"{G}Sisesta nimi: {R}")
        password = input(f"{G}Sisesta parool: {R}")
        login, user_login_status = auth(username, password, usernames, passwords, emails)

    elif func_choice == 3:
        print("Nime või parooli muutmine.")
        sleep(0.5)
        username = input(f"{G}Sisesta nimi: {R}")
        change_credentials(usernames, passwords, username, login, user_login_status, emails)

    elif func_choice == 4:
        print("Unustanud parooli taastamine.")
        sleep(0.5)
        username = input(f"{G}Sisesta nimi: {R}")
        restorePassword(user_login_status, login, username, usernames, passwords, emails)
    
    elif func_choice == 5:
        print("Lõpetamine...")
        sleep(1)
        break
