import random
def roll():
    return random.randint(1, 6)

print("\nWelcome to the Dice Game!\n")

while True:
    players = input("Enter number of players (2-4) or Q to Quit: ").lower()
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
                break
        else:
            print("Invalid number of players. Please enter a number between 2 and 4. ")
    elif players == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number between 2 and 4 or Q to Quit. ")

maximum_score = 50 
player_scores = [0 for _ in range(players)]

while max(player_scores) < maximum_score:
      
    for player_index in range(players):
        current_score = 0
        print("\nPlayer", player_index + 1, "turn\n")
        print("Current Score:", player_scores[player_index],"\n")
                
        while True:
            should_roll = input("Do you want to roll the dice? (y/n): ").lower()
            if should_roll != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! No points this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your current score is:", player_scores[player_index] + current_score)
                continue
            
            print("Invalid input. Please enter 'y' to roll or 'n' to hold.")
        player_scores[player_index] += current_score
        print("Player", player_index + 1, "total score is:", player_scores[player_index])
        
maximum_score = max(player_scores)
winning_index = player_scores.index(maximum_score)
print("player number", winning_index + 1, "wins with a score of", maximum_score)