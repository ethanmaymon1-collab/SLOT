import random
import os
import sys
import time

SYMBOLS = ["SOAKED", "WESPURYY", "TRYSTONS", "PAMELI", "CHEATMAXXER"]
BET = 10
WIN_AMOUNT = 100


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def spin_reels():
    return [random.choice(SYMBOLS) for _ in range(3)]


def print_reels(reels):
    print("+-----------------------------+")
    print(f"| {reels[0]:^9} | {reels[1]:^9} | {reels[2]:^9} |")
    print("+-----------------------------+")


def spin_animation():
    for _ in range(8):
        reels = spin_reels()
        print_reels(reels)
        time.sleep(0.12)
        clear_screen()


def main():
    balance = 1000
    clear_screen()
    print("=== SOAKEDVERSE: TERMINAL HOUSE NEVER WINS ===")
    print("Press Enter to start, type q to quit anytime.")
    input()

    while True:
        if balance < BET:
            print("OUT OF CREDITS. GAME OVER.")
            break

        clear_screen()
        print("=== SOAKEDVERSE TERMINAL SLOT ===")
        print(f"Credits: ${balance}")
        print("[ENTER] Spin  |  [Q] Quit")
        choice = input("> ").strip().lower()
        if choice == "q":
            break

        balance -= BET
        print("Spinning...")
        spin_animation()
        reels = spin_reels()
        print_reels(reels)

        if reels[0] == reels[1] == reels[2]:
            balance += WIN_AMOUNT
            print(f"JACKPOT! You win ${WIN_AMOUNT}!")
        elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
            balance += BET * 2
            print("Nice! Two matching symbols. You win $20!")
        else:
            print("No match. Try again.")

        print(f"Credits: ${balance}")
        print("Press Enter to continue or type q to quit.")
        if input("> ").strip().lower() == "q":
            break

    print("Thanks for playing. See you again in SOAKEDVERSE.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting slot machine.")
        sys.exit(0)
