# 🪨📄✂️ Rock Paper Scissors Game - Python

A simple **Rock Paper Scissors** game built in Python. This project uses the `random.randint()` function to simulate a computer opponent and basic control logic to determine the winner.

---

## 🚀 Features

- Console-based gameplay
- Play against the computer
- Random computer moves using `random.randint()`
- Clear winner/draw logic
- Option to replay the game

---

## 🧠 Game Logic

1. **User Input:**  
   The player selects one of: `"rock"`, `"paper"`, or `"scissors"`.

2. **Computer Move (Using `randint`):**  
   A random integer between 1 and 3 is generated:
   - 1 = Rock
   - 2 = Paper
   - 3 = Scissors

3. **Compare Moves:**
   - Rock beats Scissors  
   - Scissors beats Paper  
   - Paper beats Rock  
   - Same choice results in a draw

4. **Display Results:**  
   The outcome is printed and the user is asked if they want to play again.

---

## 🧾 Sample Code Snippet

```python
import random

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_number = random.randint(1, 3)
    computer_choice = options[computer_number - 1]

    print(f"\nYou chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        break
```

---

## 📦 Requirements

- Python 3.x  
  No additional libraries are required.

---

## 🏁 How to Run

1. Copy the code into a `.py` file (e.g., `rps_game.py`)
2. Open terminal or any IDE
3. Run the script:

```bash
python rps_game.py
```

---

## 🎯 What You’ll Learn

- Using `random.randint()` for decision-making
- Handling user input
- Writing game logic with conditionals
- Looping for repeated play

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ✍️ Author

**Shafin Uddin**

---

Have fun playing and feel free to improve the logic!
