import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=<>?{}[]?/:"
length_p = int(input("Enter the length of the password: "))
a = "".join(random.sample(password, length_p))

print(f"Your password is {a}")
