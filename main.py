from tkinter import *
import pandas as pd
import random
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- generate words ------------------------------- #
final_flashcard = pd.DataFrame(data={'French': ['placeholder'], 'English': ['placeholder']})
# read csv to pandas DataFrame
try:
    to_learn = pd.read_csv("to_learn.csv")
except FileNotFoundError:
    to_learn = pd.read_csv("data/french_words.csv")
if len(to_learn) >= 1:
    current_word = to_learn.sample()
else:
    # d = {'French': ['yay'], 'English': ['you win']}
    current_word = final_flashcard


def next_card():
    global to_learn
    global current_word
    global flip_timer
    window.after_cancel(flip_timer)
    if len(to_learn) >= 1:
        new_word = to_learn.sample()
    else:
        if len(to_learn) < 1:
            canvas.itemconfig(word, text="yay!", fill="black")
            canvas.itemconfig(language, text='you win!', fill="black")
            window.after_cancel(flip_timer)
            messagebox.showinfo(message='you have learned all the words from your current word list')
    canvas.itemconfig(word, text=new_word['French'].to_string(index=False), fill="black")
    canvas.itemconfig(language, text='French', fill="black")
    canvas.itemconfig(card, image=front_img)
    current_word = new_word
    # print(current_word)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- flip card ------------------------------- #
def flip_card():
    global back_img
    global current_word
    canvas.itemconfig(card, image=back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_word['English'].to_string(index=False), fill="white")


# ----------------------- update word list --------------------------- #
# remove the words the user has learned

def remove_word():
    global to_learn
    index = current_word.index
    to_learn.drop(index=index, inplace=True)
    to_learn.to_csv("to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard app")
window.config(padx=10, pady=10, bg="#B1DDC6")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg="#B1DDC6")
front_img = PhotoImage(file="images/card_front.png")
card = canvas.create_image(0, 0, image=front_img, anchor="nw")

back_img = PhotoImage(file="images/card_back.png")
# canvas.create_image(0, 0, image=front_img, anchor="nw")

language = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text=current_word['French'].to_string(index=False), fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.config(borderwidth=0)
right_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.config(borderwidth=0)
wrong_button.grid(column=1, row=1)
if len(to_learn) < 1:
    canvas.itemconfig(word, text="yay!", fill="black")
    canvas.itemconfig(language, text='you win!', fill="black")
    window.after_cancel(flip_timer)
    messagebox.showinfo(message='you have learned all the words from your current word list')
window.mainloop()


print(to_learn)
print(len(to_learn))
