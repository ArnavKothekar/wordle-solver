#-----------------------------------------------------------------
# Program: wordle_solver.py
# Author: Arnav Kothekar
# Created: 2025-05-29
# Description:
#   Interactive Wordle solver that takes your previous guesses and
#   feedback to suggest the next best word from the allowed list.
#-----------------------------------------------------------------

#Credits to M Somervile (dracos) for Wordle valid words list:
#https://gist.github.com/dracos

def load_words(filename):
    with open(filename, "r") as f:
        return [w.strip().lower() for w in f if len(w.strip()) == 5]
    
def comparison(guess, answer):
    global feedback
    feedback = ["-", "-", "-", "-", "-"]
    remaining = []
    for i in range(5):
        if guess[i] == answer[i]:
            feedback[i] = "G"
        else:
            remaining.append(answer[i])
    for i in range(5):
        if feedback[i] == "-" and guess[i] in remaining:
            feedback[i] = "Y"
    print(feedback)
    return feedback

def update_constraints(guess, feedback, greens, yellows, grays):
    for i in range(5):
        letter = guess[i]
        if feedback[i] == "G":
            greens[i] = letter
        elif feedback[i] == "Y":
            yellows.setdefault(letter, set()).add(i)
    for i in range(5):
        if feedback[i] == "-":
            letter = guess[i]
            if letter not in greens and letter not in yellows:
                grays.add(letter)

def matches_greens(w, greens):
    for i in range(5):
        if greens[i] is not None and w[i] != greens[i]:
            return False
    return True

def matches_yellows(w, yellows):
    for letter, banned in yellows.items():
        if letter not in w:
            return False
        if any(w[pos] == letter for pos in banned):
            return False
    return True

def matches_grays(w, grays):
    return not any(letter in w for letter in grays)

def filter_candidates(words, greens, yellows, grays):
    return [w for w in words if matches_greens(w, greens) and matches_yellows(w, yellows) and matches_grays(w, grays)]

#Initialization
greens  = [None, None, None, None, None]
yellows = {}
grays   = set()
word_list = load_words("wordle_valid_words.txt")
attempt = 0
guess = "audio"

#Input Answer (with validation)
while True:
    answer = input("Enter the 5 letter answer: ")
    answer = answer.lower()
    if answer not in word_list or len(answer) != 5:
        print("Answer is not a valid Wordle word.")
        continue
    break

#Main Loop
while True:
    attempt += 1
    print(f"\nGuess #{attempt}:")
    print(list(guess))
    feedback = comparison(guess, answer)

    if feedback == ["G"]*5:
        print(f"\nFound it in {attempt} guesses!")
        break

    update_constraints(guess, feedback, greens, yellows, grays)
    cands = filter_candidates(word_list, greens, yellows, grays)
    print(f"{len(cands)} possible words remain...")

    guess = cands[0]
