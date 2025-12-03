import random
while True: #LOOP RUNS ALL THE TIME 
    choice = input('Roll the dice ? (y/n) : ').lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif choice == 'n':
        print('Thanks for playing !')
        break
    else:
        print('Invalid Choice !')
        # User wants to roll two die until he enters n = terminate (break if n) if n #So LOOP
         #ASK:roll the dice? y/n
         #If y
         #Generate two random integers in range 1 to 6
         #If n
         #Print thank you message
         #Terminate
         #Else 
         #Invalid choice
