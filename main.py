from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


# UI

# Window setup
window = Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash cards")


# Canvas setup
canvas = Canvas(
    width=800,
    height=526,
    background=BACKGROUND_COLOR,
    highlightthickness=0
)
front_card_img = PhotoImage(file="images/card_front.png")

back_card_image = PhotoImage(file="images/card_back.png")

# canvas.create_image(406, 263, image=front_card_img)
canvas.create_image(400, 263, image=back_card_image)

info_text = canvas.create_text(
    400, 150, text="The Lang Name", fill="black", font=("Arial", 40, "italic"))

word_text = canvas.create_text(
    400, 263, text="The Word", fill="black", font=("Arial", 60, "bold"))

canvas.grid(column=0, row=1, columnspan=2)

# buttons

wrong_image = PhotoImage(file="images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=2)


window.mainloop()
