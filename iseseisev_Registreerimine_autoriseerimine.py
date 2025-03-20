from MyModule import *
from time import sleep
from os import system
system('title @melon3000')


#test
#------------------------------------------
print("checkpassword()", end=' -> ')
print(checkpassword('koahkoakoa123@!gG')) 
sleep(3)
system('cls')
#------------------------------------------


current_user = ""

users = {
    "user1": "password123",
    "admin": "securePass!",
    "john_doe": "qwerty123"
}

register(users)
print(users)