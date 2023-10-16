# import numpy as np
# numbers = []

# for i in range(10):
#     user_input = int(input("Please enter an integer: "))
#     numbers.append(user_input)

# total = sum(numbers)
# average = np.mean(numbers)

# print(f"The sum of these integers is: {total}")
# print(f"The average of these integers is: {average}")

# Creating a dictionary
# import random 

# random_dict = {}
# for i in range(1,11):
#     random_dict[i] = random.randint(1,100)
# print(random_dict)

# Create a pin code cracker. Let's say pin code consists of 4 random digits. 
# You can store the value in variable. Then create a loop going through all possible combinations until you find the one you entered.
import time

pin = '0000'
locked = True

start_time = time.perf_counter()
while locked:
    for digit1 in range(10):
        for digit2 in range(10):
            for digit3 in range(10):
                for digit4 in range(10):
                    current_attempt = f"{digit1}{digit2}{digit3}{digit4}"
                    if current_attempt == pin:
                        print(f"Pin Cracked! The correct pin is: {current_attempt}")
                        locked = False

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f'Elapsed time: {elapsed_time} seconds')

# all_users = {"aaa": "111", "bbb": "222", "ccc": "333"}
# value = True
# while value == True:
#     entered_username = input("Enter your username: ")
#     entered_password = input("Enter your password: ")
    
#     for username, password in all_users.items():
#         if entered_username == username and entered_password == password:
#             print("Welcome")
#             value = False 
#             break
#         else:
#            print("Wrong")
