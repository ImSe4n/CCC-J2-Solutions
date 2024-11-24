emotion = input()
happy = emotion.count(":-)")
sad = emotion.count(":-(")

if happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
else:
    print("sad")