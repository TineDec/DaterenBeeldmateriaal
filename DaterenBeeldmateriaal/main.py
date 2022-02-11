from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import *
import tkinter as tk

interface = tk.Tk()
interface.configure(bg="#60c1c9")
interface.geometry("1200x700+30+30")

#kleurcode lichtblauw = #60c1c9
#kleurcode geel = #fdc20b
#kleurcode roze = #ea94aa
#kleurcode groen = #00a57

titel = tk.Label(interface, text="DATEREN VAN BEELDMATERIAAL")
titel.configure(bg="#60c1c9", fg="#000000", font=("Calibri",20,"bold"), padx=500, pady=30)

#OPTIE 1: op basis van foto-techniek
#OPTIE 2: op basis van bezienswaardigheden
    #doorzoek thesaurus op vaste woorden

lijst = ['Tine', 'Saar', 'Flore']

frame = Frame(interface, bg='#f25252')
frame.pack(expand=True)

Label(
    frame,
    text = "Duid hier aan wat te zien is op de foto. Zoektermen moeten in het Nederlands en enkelvoud genoteerd worden.",
    bg="#60c1c9",
    fg="#000000",
    padx=5,
    pady=15,
    font = ("Calibri",12)
).pack()
#frame.place(x=30, y=30, width=1000, height=20)
#https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/ --> posities aanpassen. Kunnen we van pack terug naar grid gaan?

entry = AutocompleteCombobox(
    frame,
    width=30,
    font=('Times, 18'),
    completevalues=lijst
)
entry.pack()
#entry.place(x=80, y=130, width=300, height=50)

entry_2 = AutocompleteCombobox(
    frame,
    width=30,
    font=('Times, 18'),
    completevalues=lijst,
    )
entry_2.pack()

entry_3 = AutocompleteCombobox(
    frame,
    width=30,
    font=('Times, 18'),
    completevalues=lijst
)
entry_3.pack()



#OPTIE 3: op basis van fotograaf
#OPTIE 4: overige (zoals kartelrand, KIK-nummer bv. B0...)
#KIK-nummer = "opgelet! Je geeft aan dat de foto een KIK-nummer bevat. Het originele beeld is dan ook terug te vinden in de dataabase van het KIK. Kijk daar of de foto gedateerd is."
#Zowel één datering als overzicht + waarschuwing dat je altijd moet controleren

interface.mainloop()