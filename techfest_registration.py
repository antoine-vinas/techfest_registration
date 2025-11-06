print("Welcome to SMIT TechFest!")
print("Event organized by Antoine Viñas of APPDAET BTIS2A")

num = int(input("How many participants will register? "))

if num <= 0:
    print("Invalid number of participants.")
    exit()
else:
    print(f"{num} participants will be registered.\n")
