import random
print(" ======= (Tic, Tac and Toe game) =======")
a = int(input("Enter the start range: "))
b = int(input("Enter the end range: "))
c = []
for i in range(a, b):
    c.append(i)
d = random.choice(c)
e = 7
for i in range(e):
    print("You have only seven attempt to guess")
    f = int(input("Enter the guess number: "))
    if f < d:
        print("Too small !")
    elif f > d:
        print("Too high !")
    else:
        f == d
        print("Congratultion !")
        break;