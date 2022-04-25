import random

def get_valid_integer(message,number_range,user_picks_option):
    if not user_picks_option:
        user_input = random.choice(number_range)
    else:
        waiting_for_valid_response = True
        while waiting_for_valid_response:
            user_input = int(input(message))
            if user_input not in number_range:
                print(f'Please enter an integer 1-{number_range[-1]}')
            else:
                waiting_for_valid_response = False
    return user_input

def get_y_or_n_from_user(input_message):
    waiting_for_valid_response = True
    while waiting_for_valid_response:
        user_input = (input(input_message)).upper()  
        if user_input == 'Y' or user_input == 'N':
            waiting_for_valid_response = False
        elif user_input == 'YES':
            user_input = 'Y'
            waiting_for_valid_response = False
        elif user_input == 'NO':
            user_input = 'N'
            waiting_for_valid_response = False
        else:
            print(f'You entered {user_input}')    
            print('Your response must be either a y (Yes) or n (No)')  
    return user_input