# Python Mini Projects Collection

A set of 5 beginner-to-intermediate level Python mini projects built using standard libraries like `random`, `string`, and `file I/O`. These projects cover password validation, generation, user authentication, CLI-based banking simulation, guessing games, and a classic Snake-Water-Gun game.

---

## Project List

### 1. Password Checker

Features:
- Validates password strength based on criteria:
  - Minimum length (8)
  - At least one uppercase, lowercase, digit, special character
  - No spaces allowed

Usage:
Run the script and input a password when prompted. It returns feedback on strength or missing elements.

---

### 2. Password Generator + Checker

Features:
- Lets user decide to generate or input password
- Automatically creates a strong password or validates user input
- Reuses logic from Project 1 for checking

Usage:
Run the script and answer `yes` or `no`:
- `yes` → generates a strong password
- `no` → asks for your own password and checks it

---

### 3. ATM Simulator with User Class

Features:
- Simulates an ATM with login and account creation
- Includes:
  - Account creation with password validation or generation
  - Balance check, deposit, withdrawal, and password change
- Built with OOP (classes: `User`, `ATM`)

Usage:
Run the script and navigate through the menu:
1. Create account
2. Login
3. Use ATM menu options

All passwords are checked for strength (reuses password checker logic).

---

### 4. Guess the Number Game

Features:
- Random number (1–100) guessing game
- Tells if your guess is higher/lower
- Tracks number of attempts
- Saves high score to `score.txt`

Usage:
Run the script and guess numbers until correct.
- Output displays attempt count
- Result saved to file

File Generated:  
`score.txt` stores attempt history.

---

### 5. Snake-Water-Gun Game

Features:
- Classic 5-round game vs computer
- Rules similar to rock-paper-scissors
- Tracks scores and declares a winner
- Results saved to `score.txt`

Usage:
Run the script and enter choice:
- 1 for Snake
- 2 for Water
- 3 for Gun

Final score is displayed and saved.

---

## Requirements

- Python 3.x
- No external libraries required (only `random` and `string`)

---

## Output Files

- `score.txt` — used by Projects 4 & 5 to save scores/history.

---

## How to Run

Clone or download the files and run any project via:

```bash
python filename.py
