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

game_images=(rock,paper,scissors)
user_choice =int(input("what is your choice  o of rock, 1 for paper or  2 for scissors"))
print(user_choice)
if user_choice<=2 and user_choice>=0:
   print(game_images[user_choice])
computer_choice = random.randint(0,2)
print(computer_choice)
print(game_images[computer_choice])
if user_choice>=3 or user_choice<0:
    print("its  an invalid number")
elif computer_choice == 0 and user_choice == 2:
    print("you lose,hehe>-<")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice>user_choice:
    print(" you lose,hehe>-<")
elif user_choice>computer_choice:
    print("you win!")
elif user_choice==computer_choice:
    print("its an draw,opps")
