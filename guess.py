import random

while True:
    secret = random.randint(1,100)
    guess = 0
    attempts = 0

    while guess != secret and attempts < 7:
        guess = int(input("Угадай число: "))
        attempts = attempts +1
        if guess == secret:
            print("Угадал!")
        elif guess < secret:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
    if guess == secret:
        print("Ты справился за", attempts, "попыток")
    else:
        print("Ты проиграл. Было загадано:", secret)
    again = input("Сыграем ещё раз? (да/нет): ")
    if again != "да":
        break
