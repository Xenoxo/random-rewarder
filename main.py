import random
import matplotlib.pyplot as plt
import numpy as np
import statistics

# num = random.random()

# def num_squared (num):
#     return num ** 2

# print(num)


# x = np.linspace(0, 5, 100)

# def f(x):
#     return np.exp(x)

# plt.plot(x, f(x))

# plt.show()

def get_reward():
    tiers = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
    probabilities = [0.6, 0.25, 0.1, 0.04, 0.01]
    rarity = random.choices(tiers, weights=probabilities, k=1)[0]
    color = ''
    WHITE = '\033[37m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    RED = '\033[31m'
    RESET = '\033[0m'
    reward = 0
    if rarity == "Common":
        reward = 300
        color = WHITE
    elif rarity == "Uncommon":
        reward = 900
        color = GREEN
    elif rarity == "Rare":
        reward = 1800
        color = BLUE  
    elif rarity == "Epic":
        reward = 5400
        color = PURPLE   
    elif rarity == "Legendary":
        reward = 10800
        color = RED
    formatted_rarity = color + rarity.upper() + RESET
    return reward, formatted_rarity

print("\n\nWelcome to the rewards machine! Would you like to spin the wheel? (y/n)")

response = input()
keep_playing = True
while response != 'n':
    reward, formatted_rarity = get_reward()
    print(f"\nYou pulled a {formatted_rarity} piece of loot! You are rewarded with {reward} seconds!")
    print("Go again? (Press any key to go again, type \"n\" to end the game)")
    response = input().lower()

print("Thanks for playing ya bub!")


# print('\033[32m' + 'This text is green!' + '\033[0m')
# print('\033[34m' + 'This text is blue!' + '\033[0m')
# print('\033[35m' + 'This text is purple!' + '\033[0m')
# print('\033[33m' + 'This text is orange!' + '\033[0m')
# print('\033[37m' + 'This text is white!' + '\033[0m') 


# results = [get_reward()[0] for _ in range(10000)]
# mean = statistics.mean(results)
# print(mean)