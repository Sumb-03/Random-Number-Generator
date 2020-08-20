import random
from tkinter import*

# Window

window = Tk()
window.title('Random Number Generator')
window.maxsize(600, 300)
window.minsize(600, 300)
window.config(bg='#E5E500')

# Generate the Random Number

def generate():
    final_number_entry.delete(0, END)
    min_number = min_entry.get()
    max_number = max_entry.get()
    min_entry.delete(0, END)
    max_entry.delete(0, END)
    final_number = str(random.randint(int(min_number), int(max_number)))
    final_number_entry.insert(0, final_number)

# Inside window looks

inside_title = Label(window, text='Random Number Generator', font=('Agency FB', 35), fg='#000066', bg='#E5E500')
inside_title.place(x=100, y=20, width=400)
min_entry = Entry(window, width=30, borderwidth=5)
min_entry.place(x=230, y=110)
max_entry = Entry(window, width=30, borderwidth=5)
max_entry.place(x=230, y=150)
min_label = Label(window, text='Min', font=('Agency FB', 20), bg='#E5E500')
min_label.place(x=180, y=105)
max_label = Label(window, text='Max', font=('Agency FB', 20), bg='#E5E500')
max_label.place(x=180, y=145)
final_number_entry = Entry(window, width=38, borderwidth=5)
final_number_entry.place(x=184, y=200)
generate_button = Button(window, text='Generate', width=15, height=1, font=('Agency FB', 20), fg='white', bg='#000066', command=generate)
generate_button.place(x=225, y=235)



window.mainloop()