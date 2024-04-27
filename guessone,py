import random

low = int(input("Enter lower bound: "))
up = int(input("Enter upper bound: "))

score = 0
games = 0
while True:
    games += 1
    print("\nNew Game\n")
    c = random.randrange(low, up)

    while True:
        d = int(input(f"Guess a number between {low} and {up} (enter 0 to exit): "))

        if d == 0:
            print("Exiting the program.")
            break

        if d == c:
            print(f"Yes! You guessed right. The number is indeed {c}")
            score += 1
            break
        else:
            if d > c:
                print("Guess lower.")
            else:
                print("Guess higher.")

    if d == 0:
        break

print(f"You got {score} right out of {games} games.")
