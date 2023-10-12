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

# pin = '4981'
# locked = True

# while locked:
#     for digit1 in range(10):
#         for digit2 in range(10):
#             for digit3 in range(10):
#                 for digit4 in range(10):
#                     current_attempt = f"{digit1}{digit2}{digit3}{digit4}"
#                     # Check if the current combination matches the pin
#                     if current_attempt == pin:
#                         print(f"Pin Cracked! The correct pin is: {current_attempt}")
#                         locked = False
