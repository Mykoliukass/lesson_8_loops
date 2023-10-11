# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check ff credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials'
#  and ask to enter password and username again. The program should show numbers of times you tried to enter both credentials.
# For storing account information use dict , all data should be lowercase. and extra symbols (@, %, $ etc and numbers). 
# If in password numbers or symbols are not provided, the program should add additional value to dictionary as a value, 
# names 'improved password'
# Count how many times the user inserted a wrong password
# users_credentials = "username='mykolas2',password='jerutis2';username='eteris',password='uzimtas;username='burbulas',password='burbuliene;username='pilvas',password='didelis!;username='vardas',password='slaptazodis'"

users_credentials = input("Please insert a database to be used for users credentials: ")
credential_pairs = users_credentials.split(";")
cleaned_pairs = [pair.replace("'", "").strip() for pair in credential_pairs]
credentials_dictionary = {}
for single_pair in credential_pairs:


# while True:
#     user_input = input("Enter your name: ")
#     if len(user_input) != 0:
#         break
# print(f"You entered {user_input }")