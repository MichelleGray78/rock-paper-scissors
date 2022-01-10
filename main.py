import random

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

#Write your code below this line 👇
computer_choice = random.randint(0, 2)
player_choice = int(
    input(
        "What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: \n"
    ))

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    game_images = [rock, paper, scissors]
    print(f"Computer chose: {game_images[computer_choice]}")
    print(f"You chose: {game_images[player_choice]}")
    if player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose")
    elif computer_choice > player_choice:
        print("You lose")
    elif player_choice > computer_choice:
        print("You win!")
    elif player_choice == computer_choice:
        print("It's a draw")
