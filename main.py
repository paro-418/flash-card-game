from tkinter import *
import pandas
import random

BACKGROUND_COLOR = '#B1DDC6'

data = pandas.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')
print(to_learn)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background =canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill = 'black')
    canvas.itemconfig(card_background, image = card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text='English', fill = 'white')
    canvas.itemconfig(card_word, text=current_card['English'], fill= 'white')
    canvas.itemconfig(card_word, text=current_card['English'])
    canvas.itemconfig(card_background, image = card_back_img)


flip_timer = window.after(3000, func=flip_card)
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, command=next_card, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = Button(image=check_image, command=next_card, highlightthickness=0)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
