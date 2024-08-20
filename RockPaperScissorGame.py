import random
# Rock Paper Scissor Game

def game(Comp,you):
    if Comp == you:
        return None
    elif Comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif Comp == 'p':
            if you == 'r':
                return False
            elif you == 's':
                return True
    elif Comp == 's':
            if you == 'p':
                return False
            elif you == 'r':
                return True

print("Comp Turn: Rock(r) Paper(p) Scissor(s)?")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    Comp = 'r'
elif randNo == 2:
    Comp = 'p'
elif randNo == 3:
    Comp = 's'

you = input("Your Turn: Rock(r) Paper(p) Scissor(s)?")

a = game(Comp, you)

print(f"Computer chose {Comp}")
print(f"You chose {you}")
if a == None:
    print("The game is a tie!")
elif a:
    print("Yow Win!")
else:
    print("You Lose!")




