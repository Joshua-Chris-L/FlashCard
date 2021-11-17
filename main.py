from tkinter import *
import pandas
import random

# -----------------------------   -----------------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT1 = "Arial 40 italic"
FONT2 = "Arial 60 bold"

# ----------------- Data ---------------------------------------
data = {}
try:
    df = pandas.read_csv("images/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("images/french_words.csv")
    data = original_data.to_dict(orient="records")
else:
    data = df.to_dict(orient="records")

current_data = random.choice(data)
choice = current_data["French"]
choice2 = current_data["English"]


# French Data
def random_french():
    global choice
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=choice, fill="black")
    canvas.itemconfig(background_image, image=my_img)
    window.after(3000, func=random_english)


# English Data
def random_english():
    global choice2
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=choice2, fill="white")
    canvas.itemconfig(background_image, image=my_img2)


# Remove Current Card From Previous Card
def is_known():
    global current_data, data
    data.remove(current_data)
    print(current_data)
    dataa = pandas.DataFrame(data)
    dataa.to_csv("data/words_to_learn.csv", index=False)
    random_french()


# Window SetUp
window = Tk()
window.title("flashy")
window.config(padx=1, pady=1, bg=BACKGROUND_COLOR)
window.after(3000, func=random_english)

# image setup
canvas = Canvas(width=900, height=580)
my_img = PhotoImage(file="images/card_front.png")
my_img2 = PhotoImage(file="images/card_back.png")
background_image = canvas.create_image(450, 313, image=my_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
title = canvas.create_text(450, 150, text="Title", font=FONT1)
word = canvas.create_text(450, 250, text="Word", font=FONT2)

# Button
check_right = PhotoImage(file="images/right.png")
right_button = Button(image=check_right, highlightthickness=0, command=random_french)
right_button.grid(column=0, row=1)

check_wrong = PhotoImage(file="images/wrong.png")
right_button = Button(image=check_wrong, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

random_french()

window.mainloop()
