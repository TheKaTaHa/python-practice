import random

secret = random.randint(1,100)

guess = 0

attempts = 0


while guess != secret:
    guess = int(input("Угадай число: "))
    attempts = attempts +1
    if guess == secret:
        print("Угадал!")
    elif guess < secret:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
print("Ты справился за", attempts, "попыток")
