import re
import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.corpus import words

# Uncomment below if running first time
# nltk.download('words')

# Load dictionary words for optional use
dictionary_words = set(words.words())

def check_password_strength(password):
    suggestions = []
    score = 0

    # Criteria Checks
    if len(password) < 8:
        suggestions.append("Make the password at least 8 characters long.")
    else:
        score += 1

    if not re.search(r'[A-Z]', password):
        suggestions.append("Add at least one uppercase letter.")
    else:
        score += 1

    if not re.search(r'[a-z]', password):
        suggestions.append("Add at least one lowercase letter.")
    else:
        score += 1

    if not re.search(r'[0-9]', password):
        suggestions.append("Include at least one digit.")
    else:
        score += 1

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Include a special character (e.g., @, #, !).")
    else:
        score += 1

    if password.lower() in dictionary_words:
        suggestions.append("Avoid common dictionary words.")
    else:
        score += 1

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions


# GUI App
def evaluate_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength, suggestions = check_password_strength(password)
    result_label.config(text=f"Strength: {strength}", fg="green" if strength == "Strong" else "orange" if strength == "Moderate" else "red")

    suggestion_text.delete(1.0, tk.END)
    if suggestions:
        suggestion_text.insert(tk.END, "\n".join(suggestions))
    else:
        suggestion_text.insert(tk.END, "Your password is strong!")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.config(bg="#f0f0f0")

tk.Label(root, text="Enter Password:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
entry = tk.Entry(root, show='*', font=("Arial", 12), width=30)
entry.pack()

tk.Button(root, text="Check Strength", font=("Arial", 12), command=evaluate_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
result_label.pack(pady=5)

suggestion_text = tk.Text(root, height=6, width=40, font=("Arial", 10))
suggestion_text.pack()

root.mainloop()
