import random
from game_data import data 
from art import logo, vs
import os

def format_data(account):
    """hint2 Take the account data and returns the printable format."""
    # print(f"Compare A: {data[numbers[0]]['name']}, a {data[numbers[0]]['description']}, from {data[numbers[0]]['country']}.")
    # print(vs)
    # print(f"Against B: {data[numbers[1]]['name']}, a {data[numbers[1]]['description']}, from {data[numbers[1]]['country']}.")
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """4.2 Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        # if guess == "a":
        #    return True
        return guess == "a"   # guess是a返回的是true, 否则返回的是False
    
    else:
        return guess == "b"


# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # hint1 Generate a random account from the game data
    # 我的答案
    # def choose_data(numbers):
    #     while len(numbers) < 2:
    #         num = randint(0, len(data) - 1)
    #         if num not in numbers:
    #             numbers.append(num)
    #     return numbers
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    #hint2 Take the account data and returns the printable format.
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #hint 3 Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #hint 4 Check if user is correct.
    ## 4.1 Get follower count of each account
    # def compare_ab(a, b):
    #     if a >= b:
    #         return a        
    #     else:
    #         return b
    # def guess_higher(guess, list):
    #     if guess == "a":
    #         guess_higher = data[list[0]]['follower_count']
    #     else:
    #         guess_higher = data[list[1]]['follower_count']
    #     return guess_higher
    # higher = compare_ab(data[numbers[0]]['follower_count'], data[numbers[1]]['follower_count'])
    #         guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #         guess_higher_number = guess_higher(guess, numbers)
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    ## 4.2 Use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #hint 5 Give user feedback on their guess.
    # os.system('clear')
    # if higher == guess_higher_number:
    #     score += 1
    #     print(logo)
    #     print(f"You're right! Current score: {score}.")
        
    # else:
    #     print(logo)
    #     print(f"Sorry, that's wrong. Final score: {score}")
    #     is_gameover = True
    os.system('clear')
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")







