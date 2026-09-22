import time
import random

print("Welcome to the Reaction Time Game!")
print("When you see 'GO!', press Enter as fast as you can.")
input("Press Enter to begin...")

attempts = 5
reaction_times = []

for i in range(attempts):
    print(f"--- Attempt {i + 1} of {attempts} ---")
    print("Get ready...")

    # Wait for a random amount of time between 2 and 5 seconds
    wait_duration = random.uniform(2, 5)
    time.sleep(wait_duration)

    print("GO!")

    # Record the time when "GO!" appears
    start_time = time.monotonic()

    # Wait for the player to press Enter
    input()

    # record the time when the player presses Enter
    end_time = time.monotonic()

    # this was to calculate and display the player's reaction time
    reaction_time = end_time - start_time
    reaction_times.append(reaction_time)
    print(f"Your reaction time was: {reaction_time} seconds")

# After all 5 attempts, display the player's fastest reaction time
fastest_time = min(reaction_times)
print("--------------------")
print(f"Game Over! Your fastest reaction time was {fastest_time} seconds.")