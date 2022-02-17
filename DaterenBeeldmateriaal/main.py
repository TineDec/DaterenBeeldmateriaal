from ttkwidgets.autocomplete import AutocompleteEntryListbox
from tkinter import *
import tkinter as tk

interface = tk.Tk()
interface.configure(bg="#60c1c9")
interface.geometry('1000x2000')

#kleurcode lichtblauw = #60c1c9
#kleurcode geel = #fdc20b
#kleurcode roze = #ea94aa
#kleurcode groen = #00a57

titel = Label(interface, text="DATEREN VAN BEELDMATERIAAL")
titel.configure(bg="#60c1c9", fg="#000000", font=("Calibri",20,"bold"))
titel.grid(row=1, column=0)

#OPTIE 1: op basis van foto-techniek
#OPTIE 2: op basis van bezienswaardigheden
    #doorzoek thesaurus op vaste woorden

lijst = ['Tine', 'Saar', 'Flore', 'Sarrah', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h']
#zorgen dat enkel de zaken nog zichtbaar zijn zodra je een letter intypt (option list dus)

frame = Frame(interface, bg="#60c1c9")
frame.grid()

Label(
    frame,
    text = "Duid hier aan wat te zien is op de foto. Zoektermen moeten in het Nederlands en enkelvoud genoteerd worden.",
    bg="#60c1c9",
    fg="#000000",
    font = ("Calibri",12)
).grid(row=1, column=0, padx=3, pady=3)

entry_1 = AutocompleteEntryListbox(
    frame,
    width=20,
    height=10,
    font=('Times, 8'),
    completevalues=lijst
)
entry_1.grid(row=2, column=0, padx=20, pady=1)

entry_2 = AutocompleteEntryListbox(
    frame,
    width=20,
    height=10,
    font=('Times, 18'),
    completevalues=lijst,
    )
entry_2.grid(row=2, column=0, ipadx=10, ipady=10)

entry_3 = AutocompleteEntryListbox(
    frame,
    width=20,
    height=10,
    font=('Times, 12'),
    completevalues=lijst
)
entry_3.grid(row=2, column=0, padx=200, pady=100)


#OPTIE 3: op basis van fotograaf
#OPTIE 4: overige (zoals kartelrand, KIK-nummer bv. B0...)
#KIK-nummer = "opgelet! Je geeft aan dat de foto een KIK-nummer bevat. Het originele beeld is dan ook terug te vinden in de dataabase van het KIK. Kijk daar of de foto gedateerd is."
#Zowel één datering als overzicht + waarschuwing dat je altijd moet controleren

interface.mainloop()