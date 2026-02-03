import random

print("+-------+   +-------+    +-------+      ")
print("| o   o |   | o     |    | o     |   ")
print("|   o   |   |       |    |   o   |  ")
print("| o   o |   |     o |    |     o | ")
print("+-------+   +-------+    +-------+  ")
print("               ")
print("WELCOME TO THE DICE GAME!")
print("Place A Bet And Look To See If You Won!")
print("               ")
print("How it works: If you land a number between 0-50 you win double :) or else you lose :(")
print("               ")
print("All winnings will be sent to your BTC wallet! Please make one if you have't already!")
print("               ")
print("Enter q if you want to stop")

user_input = "ha"
wallet_address = input("Please enter your BTC wallet: ")
is_this_valid = False


while user_input != "q":
    random_num = random.randint(0, 100)
    user_input = input("Please enter q if you want to stop playing (Press Enter)")
    if user_input == "q":
        break
    bet_amount = int(input("Please place a bet: "))
        
    if random_num in range(0, 50):
        is_this_valid = True
    else: 
        is_this_valid = False

    if is_this_valid == True:
        print(f"Your number was: {random_num}")
        print(f"Congrats you won: { int(bet_amount) * 2}")
    else:
        print(f"Your number was: {random_num}")
        print("Sorry you lost :(")
        print("Try again?")
    
    

