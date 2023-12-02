import help


while True:
    user_score = computer_score = 0
    choice = int(input("""
               Press the following key to begin:
               1. Start Game
               2. Rules
               0. Exit
                       
               (:)>"""))
    
    if choice == 2:
        help.Rules()
    elif choice == 1:
        help.StartGame()
    elif (choice == 0):
        break

print("Goodbye!!!")