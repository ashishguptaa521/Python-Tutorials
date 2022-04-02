command = ""
started = False
while True:
    command = input(">").lower()
    if command == 'start':
        if started:
            print("The car is already started! Idiot!")
        else:
            print("Car started!")
        started = True
    elif command == 'stop':
        if not started:
            print("The car is already stopped! Bastard!")
        else:
            started = False
            print("The engine stopped!")
    elif command == 'help':
        print("Start - start the game \nstop - stop the car \nQuit - quit.")
    elif command == 'quit':
        print("Ending game.")
        break
    else:
        print("Sorry I don't understand! :'(")
