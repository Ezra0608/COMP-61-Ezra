round_numbers = []
player_totals = []
computer_totals = []
results = []

def roll_die():
    return roll_die.randint(1, 6)
print(roll_die)

import random

def roll_multiple_dice(num_dice):
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    total = sum(rolls)
    print(f"Rolled values: {rolls}")  
    return total  

print(f"Total sum: {roll_multiple_dice(3)}") 

def get_round_result(player_total, computer_total):
    if player_total > computer_total: 
        return "Win"
    elif player_total < computer_total:
        return "Lose"
    else:
        return "Draw"
    
print(get_round_result(18, 12))

def shop(score):
    global shop
    print("\nShop Menu:")
    print("1. Add +5 points (Cost: 5 points)")
    print("2. Add +15 points (Cost: 10 points)")
    print("3. Exit Shop")

    choice = input("Choose an option (1-3): ")
        
    if choice == "1" and score >= 5: 
                score += 5 
                print("You gained +5 points!")
    elif choice == "2" and score >= 10:
                score += 15
                print("You gained +15 points!")
    elif choice == "3":
            print("Exiting Shop.") 
    else:
            print("Invalid choice or insufficient choice")

    return score
    
def display_statistics(rounds, wins, draws, losses, score, round_numbers, player_totals, computer_totals, results):
        print("\n - Game Statistics -")
        print(f"Total rounds played: {rounds}")
        print(f"Wins: {wins}, Draws: {draws}, Losses: {losses}")
        print(f"Final Score: {score}")
    
        print("\nRound History:")
        for i in range(rounds):
            print(f"Round {round_numbers[i]}: Player Total: {player_totals[i]} vs Computer Total: {computer_totals[i]} -> {results[i]}")

score = 0
rounds = 0 
wins = 0
draws = 0
losses = 0

while True:
    

    print("\n--- New Round ---")
    shop_choice = input("Would you like to visit the shop? (yes/no): ").lower()
    if shop_choice == "yes":
        score = shop(score)
    
    rounds += 1
    player_total = roll_multiple_dice(2)  
    computer_total = roll_multiple_dice(2)  
    
    print(f"You rolled: {player_total}")
    print(f"Computer rolled: {computer_total}")
    
    result = get_round_result(player_total, computer_total)
    print(f"Round Result: {result}")
    
    if result == "Win":
        wins += 1
        score += 5  
    elif result == "Draw":
        draws += 1
        score += 2  
    else:
        losses += 1
        score -= 3  

    round_numbers.append(rounds)
    player_totals.append(player_total)
    computer_totals.append(computer_total)
    results.append(result)
    
    cont = input("Do you want to play another round? (yes/no): ").lower()
    if cont != "yes":
        break

display_statistics(rounds, wins, draws, losses, score, round_numbers, player_totals, computer_totals, results)
