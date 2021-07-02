import random
hidden = random.randrange(1, 10)
count=0
while count<3:
    guess = int(input("Ingresa un numero que creas: "))
    if guess == hidden:
        print("ADIVINASTE!")
        count+=3
    elif guess < hidden:
        print("Muy bajo")
        
    else:
        print("Muy alto")
        
