from tkinter import *


def calculate():
    converted_km = int(miles_entry.get()) * 1.60934
    km_result_label.config(text=str(converted_km))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Labels

miles_input = Label(text="miles")
miles_input.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

# Entry
miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)
print(miles_entry.get())

# Button

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)



window.mainloop()