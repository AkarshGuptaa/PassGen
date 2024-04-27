import random

low = int(input("Enter lower bound"))
up = int(input("Enter upper bound"))

while True:
    print("\nNew Game\n")
    c = random.randrange(low, up)
    d = int(input(f"Guess a number between {low} and {up} (enter 0 to exit): "))

    if d == 0:
        print("Exiting the program.")
        break
    if d == c:
        print(f"Yess you guessed right. The number is indeed {c}")
    else:
        print(f"Sorry, the number was {c}, not {d}")
