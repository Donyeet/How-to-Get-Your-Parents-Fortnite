while True:
    data = input("Please enter a loud message (must be all caps): ")
    if not data.isupper():
        print("Sorry, your response was not loud enough.")
        continue
    else:
        break

while True:
    data = input("Give Me Fortnite. Yes or No: ")
    if data.lower() not in ('yes'):
        print("Not an appropriate choice.")
    else:
        print("NOW GET FORTNITE! store.epicgames.com")
        break
        exit(0)
