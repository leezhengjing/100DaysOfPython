from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/final_chinese_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



# --------------------------- FUNCTIONS -------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    chinese_card = current_card["Chinese"]
    pinyin_card = current_card["Pinyin"]
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="Chinese", fill="black")
    canvas.itemconfig(card_word, text=f"{chinese_card}", fill="black")
    canvas.itemconfig(pinyin_word, text=f"{pinyin_card}", fill="black")
    window.after(3000, func=flip_card)


def flip_card():
    english_card = current_card["English"]
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(pinyin_word, text=f"")
    canvas.itemconfig(card_word, text=f"{english_card}", fill="white")


def is_known():
    to_learn.remove(current_card)
    next_card()
    print(current_card)
    to_learn_data = pandas.DataFrame(to_learn)
    to_learn_data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 90, text="Chinese", fill="black", font=("Arial", 20, "italic"))
card_word = canvas.create_text(400, 270, text="", fill="black", font=("Arial", 60, "bold"))
pinyin_word = canvas.create_text(400, 200, text="", fill="black", font=("Arial", 30, "normal"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
check_image = PhotoImage(file="./images/right.png")
cross_image = PhotoImage(file="./images/wrong.png")
correct_button = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
correct_button.grid(row=1, column=1)
wrong_button = Button(image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
