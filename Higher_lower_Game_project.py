#importing random function
import random
# art display
# vs display
# choose random names from dictionary with details like discription and country
#make a function of random to chose againt it which we want to compete



#compare themselfs from it and give output

from game_data import data
from higher_lower_logo import logo,vs
print(logo)
def Play_game():
    def formated_print(account):
        """Print the format of our programs results"""
        name=account['name']
        description=account['description']
        country=account['country']
        return f"{name}, a {description} from {country}"
    continuty=True
    score=0

    account_b = random.choice(data)
    #Use while loop for continue of program till incorrect answer
    while continuty:
        account_a = account_b
        account_b=random.choice(data)
        if account_a==account_b:
            account_b=random.choice(data)

        compare=formated_print(account_a)
        print(f"compare:Choose: A  {formated_print(account_a)}")
        print(vs)
        against=formated_print(account_b)
        print(f"Against: Choose:B {formated_print(account_b)}")

        followers_count_a= account_a['follower_count']
        followers_count_b=account_b['follower_count']

        def check_answer(guess, follower_count_a, follower_count_b):
            if followers_count_a > followers_count_b:
                return guess=='a'
            else:
                return guess=='b'

        guess= input("Which one has high number of follower 'A' or 'B': ").lower()
        is_True=check_answer(guess,followers_count_a,followers_count_b)

        if is_True:
            score+=1
            print(f'Right Answer! Your Current score is: {score}')

        else:
            continuty=False
            print(f'Incorrect Answer!, You final score is: {score}')
            play_again=input("Do you want to play again 'y' or 'n' :  \n")
            if play_again=='y':
                Play_game()

Play_game()








