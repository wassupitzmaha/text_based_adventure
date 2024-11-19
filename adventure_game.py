def start_game():
    print("Hello Adventurer! You are in a Fairytale Forest! Choose your destiny wisely! \n You are in Forest Entrance") 
    playerOneInput = input("Choose Your Path (write it as is!): \n Path 1: GO NORTH \n Path 2: CLIMB OAK TREE...")
    if playerOneInput == "GO NORTH":
        print("Looks like you didn't choose wisely...GAME OVER")
    else: 
        print("You found an old map and now you're headed West")
        print(west())
    while (playerOneInput == "GO NORTH"):
        print(start_game())
    

def west():
    print("You are now facing two paths:...")
    playerOneInput = input("Choose between the two paths: \n Path Pink or Path Purple...")
    if playerOneInput == "Path Purple":
        print("You found the treasure, YESS!")
        
    else:
        print("You got bitten by a poisonous spider")
    while (playerOneInput == "Path Pink"):
        print(west())
        break

print(start_game())






