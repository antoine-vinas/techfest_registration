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

tracks = {p['track'] for p in participants}

print("\nTracks offered in this event:")
print(", ".join(tracks))

if len(tracks) < 2:
    print("Not enough variety in tracks.")

seen = set()
duplicates = set()

for p in participants:
    name = p['name']
    if name in seen:
        duplicates.add(name)
    else:
        seen.add(name)

if duplicates:
    for d in duplicates:
        print(f"Duplicate name found: {d}")
else:
    print("No duplicate names.")

summary = {}

for p in participants:
    track = p['track']
    if track in summary:
        summary[track] += 1
    else:
        summary[track] = 1

print("\nParticipants per track:")
for track, count in summary.items():
    print(f"{track}: {count}")

