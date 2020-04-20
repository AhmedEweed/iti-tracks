from main_scrape import *
from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("Scrape ITI subjects")
window.geometry('450x250') 
dialog = StringVar()

def clicked():
    get_subjects_btn.config(state = 'disabled')
    if len(combo.get()) == 0:
        lbl2.config(text = 'Please choose a track')
        get_subjects_btn.config(state = 'normal')
    else:
        get_subjects_btn.config(state = 'disabled')
        tname = combo.get()
        scrape(get_link(tname))
        get_subjects_btn.config(state = 'normal')
        lbl2.config(text = 'Scraping done!' + '\n' + 'Check your directory')


def Exit():
    window.destroy()



lbl1= Label(window, text ='Choose your track')
lbl1.grid(column=0, row=0)

lbl2 = Label(window)
lbl2.grid(column=1, row=1)

combo_values = sorted(get_names())
combo = Combobox(window, state = 'readonly', values = combo_values)
combo.grid(column=1, row=0)

get_subjects_btn = Button(window, text= 'Get Subjects List', command=clicked)
get_subjects_btn.grid(column=3, row=0)

exit_btn = Button(window, text= 'Exit', command=Exit)
exit_btn.grid(column=3, row=2)

window.mainloop()