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

def get_seconds():
    # tiers = [1, 2, 3, 4, 5]
    tiers = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
    probabilities = [0.6, 0.25, 0.1, 0.04, 0.01]
    rarity = random.choices(tiers, weights=probabilities, k=1)[0]
    seconds = 0
    if rarity == "Common":
        seconds = 300
    elif rarity == "Uncommon":
        seconds = 900
    elif rarity == "Rare":
        seconds = 1800
    elif rarity == "Epic":
        seconds = 5400
    elif rarity == "Legendary":
        seconds = 10800
    return seconds, rarity

results = [get_seconds()[0] for _ in range(10000)]
mean = statistics.mean(results)
print(mean)

print("\n\nWelcome to the rewards machine! Would you like to spin the wheel? (y/n)")

response = input()
keep_playing = True
while keep_playing:
    seconds, rarity = get_seconds()
    print(f"You pulled a {rarity} piece of loot! You are rewarded with {seconds} seconds", )
    print("Would you like to go again? (Press any key to go again, type \"n\" to end the game)")
    response = input()
    keep_playing = response.lower() != "n"
 
print("Thanks for playing ya bub!")

# if response.lower() == "y":
#     seconds, rarity = get_seconds()
#     print(f"You pulled a {rarity} piece of loot! You are rewarded with {seconds} seconds", )
# else:
#     print("Thanks for playing ya bub!")