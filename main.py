#PYTHON SLOT MACHINE
import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))
        return result

def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100

print("***********************")
print("Welcome to Python Slots")
print("Symbols:🍒 🍉 🍋 🔔")
print("***********************")

while balance > 0:
    print(f"your current: ${balance}")

main()
