from cs50 import get_string
import string

text = get_string("Text: ")

n_words = n_sent = n_let = i = 0
length = len(text)
for i in range(length):
    # counting letters
    if text[i].isalpha():
        n_let += 1
    # counting words
    if text[i] == ' ':
        if text[i - 1].isalpha and text[i + 1].isalpha:
            n_words += 1
    # counting sentences
    if text[i] == "." or text[i] == "?" or text[i] == "!":
        n_sent += 1
    i += 1
n_words += 1
# using the given formula
L = (n_let / n_words) * 100
S = (n_sent / n_words) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

#print
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
