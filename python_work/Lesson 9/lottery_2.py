from random import choice as c

lottery_pull = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')

def generate_ticket(digits=4):
    return [c(lottery_pull) for _ in range(digits)]

def simulate_lottery(runs=1000, digits=4):
    my_ticket = generate_ticket(digits)
    results = []

    for _ in range(runs):
        iterations = 0
        rolling = True
        while rolling:
            current_ticket = generate_ticket(digits)
            iterations += 1
            if my_ticket == current_ticket:
                results.append(iterations)
                rolling = False
    
    return results

# Run the simulation
runs = 1000  # Number of simulations
results = simulate_lottery(runs)

# Analyze the results
average_draws = sum(results) / len(results)
max_draws = max(results)
min_draws = min(results)

print(f"After {runs} simulations:")
print(f"Average number of draws to win: {average_draws}")
print(f"Minimum number of draws to win: {min_draws}")
print(f"Maximum number of draws to win: {max_draws}")
