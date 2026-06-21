word = ""
motion = False
while True:
    word = input("> ")
    if word == "start":
        if motion:
            print("Car has already started.")
        else:
            print("Car started.")
            motion = True
    elif word == "stop":
        if not motion:
            print("car has already stopped moving")
        else:
            print("Car has stopped.")
            motion = False
    elif word == "help":
        print("""start - Car started... Ready to go!
stop - Car stopped.
quit - Exit game""")
    elif word == "quit":
        break
