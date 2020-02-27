from main_scrape import *
from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("Scrape ITI subjects")
window.geometry('350x200') 

def clicked():
    get_subjects_button.config(state = 'disabled')
    if len(combo.get()) == 0:
        lbl2.config(text = 'Please choose a track')
        get_subjects_button.config(state = 'normal')
    else:
        get_subjects_button.config(state = 'disabled')
        tname = combo.get()
        scrape(get_link(tname))
        get_subjects_button.config(state = 'normal')
        lbl2.config(text = 'Scraping done!' + '\n' + 'Check your directory')

def Exit():
    window.destroy()

lbl1= Label(window, text ='Choose you track')
lbl1.grid(column=0, row=0)

lbl2 = Label(window)
lbl2.grid(column=1, row=1)

combo_values = sorted(get_names())
combo = Combobox(window, state = 'readonly', values = combo_values)
combo.grid(column=1, row=0)

get_subjects_button = Button(window, text= 'Get Subjects List', command=clicked)
get_subjects_button.grid(column=3, row=0)

exit_button = Button(window, text= 'Exit', command=Exit)
exit_button.grid(column=3, row=2)

window.mainloop()