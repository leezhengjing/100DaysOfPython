from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button


def button_clicked():
    my_label.config(text="Button Got Clicked")


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Dont click me!")
new_button.grid(column=3, row=0)


# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=4, row=2)




window.mainloop()
