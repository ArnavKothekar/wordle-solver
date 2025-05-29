# 🧠 Wordle Solver v1.0.0

> **Valid Wordle words list curated by [M Somerville (dracos)](https://github.com/dracos).**

---

## 📋 What Is Wordle?

Wordle is a 5-letter word puzzle published daily by the New York times where users have **6 tries** to guess a hidden word.  
After each guess, letters light up:  
- 🟩 **Green** = correct letter **and** correct position  
- 🟨 **Yellow** = correct letter, **wrong** position  
- ⬜ **Gray** = letter **not** in the word  

---

## 🔧 v1.0.0 Functionality

1. **Load the Word List**  
   - Read `Wordle_Words.txt` into `word_list` (all valid 5-letter entries).
2. **Fixed Starter**  
   - Begin every game with your chosen starter word (`audio` by default).
3. **Compare & Get Feedback**  
   - `comparison(guess, answer)` returns a 5-char list like `["G","Y","-","-","Y"]`.
4. **Update Constraints**  
   - **Greens**: lock letters in exact positions  
   - **Yellows**: record letters that must appear elsewhere  
   - **Grays**: ban letters not present (two-phase pass to handle duplicates)
5. **Filter Candidates**  
   - `filter_candidates(word_list, greens, yellows, grays)`  
   - Keeps only words matching **all** current constraints.

## 🛠️ Plans for Future Improvements (v1.x+)

- **Smarter Guess Selection**: Implement letter-frequency or entropy-based heuristics to choose higher-impact next guesses.  
- **Hard-Mode Support**: Enforce re-use of all revealed green/yellow letters in subsequent guesses.  
- **Basic UI or CLI Flags**: Add command-line options (e.g., custom starter word, verbose mode) or a simple web interface for easier use. 

