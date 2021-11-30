from tkinter import *
from random import choice
import csv

BACKGROUND_COLOR = "#B1DDC6"
card = {}
learning_list = []

# Create new flash cards
temp_card_list = []
try:
    with open("data/french_words_to_learn.csv", newline='') as file:
        temp_elem_list = csv.reader(file)
except FileNotFoundError:
    with open("data/french_words.csv", newline='') as file:
        temp_elem_list = csv.reader(file)
        for row in temp_elem_list:
            temp_card_list.append(row)
else:
    for row in temp_elem_list:
        temp_card_list.append(row)

lang = temp_card_list[0][0]
to_lang = temp_card_list[0][1]
temp_card_list.pop(0)
for elem in temp_card_list:
    dict_card = {lang: elem[0], to_lang: elem[1]}
    learning_list.append(dict_card)


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
    global card
    learning_list.remove(card)
    with open("data/french_words_to_learn.csv", "w") as data:
        for elem in learning_list:
            data.write(f"{elem['French']},{elem['English']}")
            data.write("\n")
    serve_card()


# UI setup
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
