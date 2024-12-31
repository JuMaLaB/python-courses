import random

god_choice = random.choice(['trump','poutine','macron'])
my_choice = input("Please choose your bastard ?\n")

print("God choose: ", god_choice)

if my_choice == god_choice == "macron":
    print("you're both idiots, you can't win with macron")    
elif my_choice == god_choice == "trump":
    print("you are both the worst bastard ever")
elif my_choice == god_choice == "poutine":
    print("you are both the 2nd worst bastard ever")
elif my_choice == "macron":
    print("of course you loose")  
elif my_choice == "trump":
    print("of course you win")
