import random

print("Welcome to the Rock, Paper and Scissors game")
user_score = 0
computer_score = 0
player_name = None

def ShowScore(player_name, user_score, computer_score):
    print(f"{player_name}: {user_score} | Computer: {computer_score}")

def Outcome(player_name, user_choice, computer_choice, store, length_of_store):
    global user_score, computer_score

    if user_choice >= length_of_store or user_choice < 0:
        print("You typed an invalid number")
    else:

        if user_choice == 0 and computer_choice == 2:
            user_score += 1
            print(f"You choose {store[user_choice]} Computer choose {store[computer_choice]}")
            print("You won this round")
        elif computer_choice == 0 and user_choice == 2:
            computer_score += 1
            print(f"You choose {store[user_choice]}\nComputer choose {store[computer_choice]}")
            print("You Lost this round")
        elif computer_choice > user_choice:
            computer_score += 1
            print(f"You choose {store[user_choice]}\nComputer choose {store[computer_choice]}")
            print("You Lost this round")
        elif user_choice > computer_choice:
            user_score += 1
            print(f"You choose {store[user_choice]}\nComputer choose {store[computer_choice]}")
            print("You won this round")
        elif computer_choice == user_choice:
            print(f"You choose {store[user_choice]}\nComputer choose {store[computer_choice]}")
            print("Tie")

        ShowScore(player_name, user_score, computer_score)

def Rules():
    print("""
            Welcome to Rock, Paper, Scissors!
            Choose your move and see if you can beat the computer. Here are the rules:
            *Rock crushes Scissors
            *Scissors cuts Paper
            *Paper covers Rock
            Choose a number to make your move, and the computer will randomly choose its move. Good luck!
        """)
    
def StartGame():
    global player_name
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    store = [rock, paper, scissors]
    length_of_store = len(store)

    print(f"    0. rock\n{store[0]}\n     1. paper\n{store[1]}\n   2. scissors\n{store[2]}")

    while True:
        if player_name == None:
            player_name = input("Input your name to start: ")

        user_choice = int(input("""
                                What do you choose? 
                                0 for Rock
                                1 for Paper
                                2 for Scissors

                                (:)>"""))
        
        computer_choice = random.randint(0, length_of_store - 1)
        
        Outcome(player_name, user_choice, computer_choice, store, length_of_store)
        is_next_round = input("Next Round y/n....").lower()
        if is_next_round == "y":
            StartGame()
        else:
            if user_score > computer_score:
                ShowScore(player_name, user_score, computer_score)
                print("Congratulations!!! You Won")
            elif computer_score > user_score:
                ShowScore(player_name, user_score, computer_score)
                print("Sorry!!! You Lose")
            else:
                ShowScore(player_name, user_score, computer_score)
                print("A Draw")
        break