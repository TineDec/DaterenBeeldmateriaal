from tkinter import Listbox

from ttkwidgets.autocomplete import AutocompleteEntryListbox
from tkinter import *
import tkinter as tk

interface = tk.Tk()
interface.configure(bg="#60c1c9")
interface.geometry('1000x2000')

def update(data):
    my_list.delete(0, END)

    for item in data:
        my_list.insert(END, item)

def check(e):
    typed = entry_1.get()

    if typed == '':
        data = lijst
    else:
        data = []
        for item in lijst:
            if typed.lower() in item.lower():
                data.append(item)
    update(data)

def fillout(e):
    entry_1.delete(0, END)
    entry_1.insert(0, my_list.get(ACTIVE))


entry_1 = Entry(interface)
entry_1.grid(row=1, column=3)
entry_1.grid()
my_list: Listbox = Listbox(interface)
my_list.grid(row=2, column=3)
my_list.grid()

my_list.bind("<<ListboxSelect>>", fillout)

#kleurcode lichtblauw = #60c1c9
#kleurcode geel = #fdc20b
#kleurcode roze = #ea94aa
#kleurcode groen = #00a57

titel = Label(interface, text="DATEREN VAN BEELDMATERIAAL")
titel.configure(bg="#60c1c9", fg="#000000", font=("Calibri",20,"bold"))
titel.grid(row=1, column=0, columnspan=2)

#OPTIE 1: op basis van foto-techniek
#OPTIE 2: op basis van bezienswaardigheden
    #doorzoek thesaurus op vaste woorden

lijst = ['Tine', 'Saar', 'Flore', 'Sarrah', 'tram met elect. bovenleidingen', 'paardentram', 'tram met paard', 'tram zonder elec. bovenleiding', 'e','f', 'g', 'h']

#frame = Entry(interface, bg="#60c1c9")
#frame.grid()

Label(
    text = "Duid hier aan wat te zien is op de foto. Zoektermen moeten in het Nederlands en enkelvoud genoteerd worden.",
    bg="#60c1c9",
    fg="#000000",
    font = ("Calibri",12)
).grid(row=1, column=1, columnspan=2, pady=20)

entry_1.bind('<KeyRelease>', check)
update(lijst)

#entry_2 = AutocompleteEntryListbox(
#   frame,
#   width=25,
#   height=10,
#   font=('Calibri, 12'),
#   completevalues=lijst,
#   )
#entry_2.grid(row=2, column=2)

#entry_3 = AutocompleteEntryListbox(
#   frame,
#   width=25,
#   height=10,
#   font=('Calibri, 12'),
#   completevalues=lijst
#)
#entry_3.grid(row=2, column=3)


#OPTIE 3: op basis van fotograaf
#OPTIE 4: overige (zoals kartelrand, KIK-nummer bv. B0...)
#KIK-nummer = "opgelet! Je geeft aan dat de foto een KIK-nummer bevat. Het originele beeld is dan ook terug te vinden in de dataabase van het KIK. Kijk daar of de foto gedateerd is."
#Zowel één datering als overzicht + waarschuwing dat je altijd moet controleren

interface.mainloop()