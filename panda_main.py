from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
card = {}
learning_list = []
# Create new flash cards

try:
    data = pandas.read_csv("data/french_words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("data/french_words.csv")
    learning_list = og_data.to_dict(orient="records")
else:
    learning_list = data.to_dict(orient="records")
# Ex. [{'French': 'partie', 'English': 'part'}]

# Fun functions


def serve_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = choice(learning_list)
    canvas.itemconfig(info_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(info_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card_img)


def i_knew_it():
    learning_list.remove(card)
    data = pandas.DataFrame(learning_list)
    data.to_csv("data/french_words_to_learn.csv", index=False)
    serve_card()


window = Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash cards")

flip_timer = window.after(3000, flip_card)

canvas = Canvas(
    width=800,
    height=526,
    background=BACKGROUND_COLOR,
    highlightthickness=0
)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=front_card_img)

info_text = canvas.create_text(
    400, 150, text="title", fill="black", font=("Arial", 40, "italic"))

word_text = canvas.create_text(
    400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# buttons

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(
    image=wrong_image,
    highlightthickness=0,
    command=serve_card
)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(
    image=right_image,
    highlightthickness=0,
    command=i_knew_it
)
right_button.grid(column=1, row=1)

serve_card()

window.mainloop()
