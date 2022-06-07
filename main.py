from tkinter import *
import pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"

df1 = pd.read_csv("data/french_words.csv")
french_words = df1.to_dict(orient="records")
random_french_word = {}
def pick_random_word():
    global random_french_word,flip_timer #stores the random french word picked in the dictionary above
    window.after_cancel(flip_timer)
    random_french_word = random.choice(french_words)
    canvas.itemconfig(card_title,text= "French",fill="black")
    canvas.itemconfig(card_word,text=random_french_word['French'],fill="black")
    canvas.itemconfig(card_background,image=card_front_image)
    flip_timer = window.after(3000,func=flip_card)
def flip_card():
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_word, text=random_french_word['English'], fill = "white")
    canvas.itemconfig(card_background, image=card_back_image)

window = Tk()
window.title("Flashcards")
window.config(padx=50,pady=50,bg =BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height = 526)
card_front_image = PhotoImage(file = "images/card_front.png")
card_back_image = PhotoImage(file = "images/card_back.png")
card_background = canvas.create_image(400, 253,image =card_front_image)
card_title = canvas.create_text(400,150,text="", font=("Arial",40,"italic"))
card_word=canvas.create_text(400, 253, text="",font=("Arial",40,"bold"))
canvas.grid(row = 0,column=0, columnspan = 2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command = pick_random_word)
unknown_button.grid(row=1,column=0)

check_image=PhotoImage(file="images/right.png")
known_button = Button(image=check_image,highlightthickness=0,command = pick_random_word)
known_button.grid(row=1,column=1)

pick_random_word()

window.mainloop()

