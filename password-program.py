# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check ff credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials'
#  and ask to enter password and username again. The program should show numbers of times you tried to enter both credentials.
# For storing account information use dict , all data should be lowercase. and extra symbols (@, %, $ etc and numbers). 
# If in password numbers or symbols are not provided, the program should add additional value to dictionary as a value, 
# names 'improved password'
# Count how many times the user inserted a wrong password
# username='mykolas2',password='jerutis2';username='eteris',password='uzimtas;username='burbulas',password='burbuliene1!;username='pilvas',password='didelis!;username='vardas',password='slaptazodis'
# "username='mykolas2',password='jerutis2';username='eteris',password='uzimtas';username='burbulas',password='burbuli;ene1!';username='pil'vas',password='didelis!';username='vardas',password='slaptazodis'"

import random, re
data_base = input("Please insert a database to be used for users credentials: ")
pairs = re.findall(r"username='(.*?)',password='(.*?)'", data_base)
credentials_dictionary = {}
for username, password in pairs:
    credentials_dictionary[username] = password
print(credentials_dictionary)
while True:
    input_username = input("Please enter your username: ")
    number_of_attempts = 0
    if input_username in credentials_dictionary:
        while True:
            input_password = input(f"Hey {input_username}! Please enter your password: ")
            if credentials_dictionary[input_username] == input_password:
                special_symbols = "!@#$%^&*()-_=+[]{}|:'\".<>?/"
                if any(symbol in special_symbols for symbol in input_password) and any(symbol.isdigit() for symbol in input_password):
                    print("Login successful!")
                else:
                    if any(symbol in special_symbols for symbol in input_password):
                        random_digit = str(random.randint(0, 9))
                        improved_password = credentials_dictionary[input_username] + random_digit 
                        print(f"Login successful! However, we would like to suggest an improved password: {improved_password}")
                    else:
                        random_symbol = random.choice(special_symbols)
                        improved_password = credentials_dictionary[input_username] + random_symbol
                        print(f"Login successful! However, we would like to suggest an improved password: {improved_password}")
                break
            else:
                number_of_attempts += 1
                print(f"Login failed. Incorrect password. You have tried to login {number_of_attempts} times")
        break
    else:
        print("Login failed. Username not found.")

