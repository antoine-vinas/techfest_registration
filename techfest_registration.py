print("Welcome to SMIT TechFest!")
print("Event organized by Antoine Viñas of APPDAET BTIS2A")

num = int(input("How many participants will register? "))

if num <= 0:
    print("Invalid number of participants.")
    exit()
else:
    print(f"{num} participants will be registered.\n")

participants = []

for i in range(num):
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")
    participants.append({"name": name, "track": track})

print("\nRegistered Participants:")
for i, p in enumerate(participants, start=1):
    print(f"{i}. {p['name']} - {p['track']}")
