YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = '\033[31m'
RESET = "\033[0m"

def checkpassword(password):
    symbols1 = list(".,:;!_*-+()/#¤%&")
    symbols2 = list("0123456789")
    symbols3 = list('qwertyuiopasdfghjklzxcvbnm')
    symbols4 = list('QWERTYUIOPASDFGHJKLZXCVBNM')

    has_symbols = False
    has_digits = False
    has_lowercase = False
    has_uppercase = False

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
            print(f'{GREEN}Parool vastab normile{RESET}.')
            return True
    print(f'{RED}Parool ei vastab normile{RESET}.')
    return False


def autopassword():
    import random
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    return psword


def register(users): #edastame sõnastiku *users*, et funktsioon vottis olevad andmeid (ehk {username:password})
    """Funktsioon loob uut kasutaja, kui tema juba ei ole loodud ja nimi pole kasutatud.
    :param users: {nimi:parool} sõnastikust,
    """
    username = input("Sisesta nimi: ")
    
    if username.lower() in (name.lower() for name in users): #kontrollime, kas user on juba registreerinud voi ei

        print("Viga! Nimi on juba kasutusel.")
        return 
    
    password_method_choice = int(input("1 - Autogenereerimine, 2 - Manuaalne: "))
    
    if password_method_choice == 1:
        users[username] = autopassword()
        print(f"Kasutaja {username} on registreeritud!")
        print("Teie parool:", users[username])
        return
        
    elif password_method_choice == 2:
        password = input("Sisesta parool: ")
        if checkpassword(password) == True:
            users[username] = password #määrame uuele kasutajale parooli ja kirjutame selle sõnastikku

            print(f"Kasutaja {username} on registreeritud!")

def auth(username:str, password:str)->any:
    """
    """

def userData_Rhange(username:str, password:str)->any:
    """
    """

def userData_Restore(username:str, password:str)->any:
    """
    """

