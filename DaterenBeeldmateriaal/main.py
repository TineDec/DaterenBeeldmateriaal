import tkinter as tk
from tkinter import *
from tkinter import Listbox
import pandas as pd

interface = tk.Tk()
interface.configure(bg="#60c1c9")
interface.geometry('1500x750')
interface.title('Dateren van beeldmateriaal')

# kleurcode lichtblauw = #60c1c9
# kleurcode geel = #fdc20b
# kleurcode roze = #ea94aa
# kleurcode groen = #00a57e

# OPTIE 1: op basis van foto-techniek
# OPTIE 2: op basis van bezienswaardigheden

titel = Label(interface, text='1. BEZIENSWAARDIGHEDEN')
titel.configure(bg="#60c1c9", fg="#000000", font=("Calibri", 20, "bold"))
titel.place(relx=0.15, rely=0, anchor=N)

# TO DO: SCROLLBAR TOEVOEGEN
# TO DO: ZORGEN DAT TEKST LEESBAAR IS IN TYPVELD (OP TWEE REGELS PLAATSEN?)

# https://stackoverflow.com/questions/43922356/how-to-read-an-excel-column-into-a-list --> lijst maken van excel d.m.v. pandas
file_name = "Gebeurtenissen_Lijst.xlsx"
xl_workbook = pd.ExcelFile(file_name)
df = xl_workbook.parse("Gebeurtenissen")
alist = df['GEBEURTENIS (PYTHON)'].tolist()
begindatum = df['Begindatum'].tolist()
einddatum = df['Einddatum'].tolist()

Label(
    text="Duid hier aan wat te zien is op de foto. Zoektermen moeten in het Nederlands en enkelvoud genoteerd worden.",
    bg="#60c1c9",
    fg="#000000",
    font=("Calibri", 12)
).place(relx=0.29, rely=0.05, anchor=N)


def update(data):
    my_list_1.delete(0, END)

    for entry in data:
        my_list_1.insert(END, entry)


def check(e):
    typed = entry_1.get()

    if typed == '':
        data = alist
    else:
        data = []
        for item in alist:
            if typed.lower() in item.lower():
                data.append(item)
    update(data)


def fillout(e):
    entry_1.delete(0, END)
    entry_1.insert(0, my_list_1.get(ACTIVE))


entry_1 = Entry(interface, width=53)
entry_1.place(relx=0.205, rely=0.12, anchor=N)
entry_1.bind('<KeyRelease>', check)

my_list_1: Listbox = Listbox(interface, height=20, width=50)
my_list_1.place(relx=0.2, rely=0.15, anchor=N)
my_list_1.bind("<<ListboxSelect>>", fillout)

scrollbar_v = Scrollbar(interface, orient=VERTICAL, command=my_list_1.yview)
scrollbar_v.place(relx=0.301, rely=0.151, height=324)
scrollbar_h = Scrollbar(interface, orient=HORIZONTAL, command=my_list_1.xview)
scrollbar_h.place(relx=0.0985, rely=0.583, width=320.5)


def update_2(data_2):
    my_list_2.delete(0, END)

    for item in data_2:
        my_list_2.insert(END, item)


def check_2(e):
    typed = entry_2.get()

    if typed == '':
        data_2 = alist
    else:
        data_2 = []
        for item in alist:
            if typed.lower() in item.lower():
                data_2.append(item)
    update_2(data_2)


def fillout_2(e):
    entry_2.delete(0, END)
    entry_2.insert(0, my_list_2.get(ACTIVE))


entry_2 = Entry(interface, width=53)
entry_2.place(relx=0.505, rely=0.12, anchor=N)
entry_2.bind('<KeyRelease>', check_2)

my_list_2: Listbox = Listbox(interface, height=20, width=50)
my_list_2.place(relx=0.5, rely=0.15, anchor=N)
my_list_2.bind("<<ListboxSelect>>", fillout_2)

scrollbar_v = Scrollbar(interface, orient=VERTICAL, command=my_list_2.yview)
scrollbar_v.place(relx=0.601, rely=0.151, height=324)
scrollbar_h = Scrollbar(interface, orient=HORIZONTAL, command=my_list_2.xview)
scrollbar_h.place(relx=0.3988, rely=0.583, width=320.5)


def update_3(data_3):
    my_list_3.delete(0, END)

    for item in data_3:
        my_list_3.insert(END, item)


def check_3(e):
    typed = entry_3.get()

    if typed == '':
        data_3 = alist
    else:
        data_3 = []
        for item in alist:
            if typed.lower() in item.lower():
                data_3.append(item)
    update_3(data_3)


def fillout_3(e):
    entry_3.delete(0, END)
    entry_3.insert(0, my_list_3.get(ACTIVE))


entry_3 = Entry(interface, width=53)
entry_3.place(relx=0.803, rely=0.12, anchor=N)
entry_3.bind('<KeyRelease>', check_3)

my_list_3: Listbox = Listbox(interface, height=20, width=50)
my_list_3.place(relx=0.8, rely=0.15, anchor=N)
my_list_3.bind("<<ListboxSelect>>", fillout_3)

scrollbar_v = Scrollbar(interface, orient=VERTICAL, command=my_list_3.yview)
scrollbar_v.place(relx=0.901, rely=0.151, height=324)
scrollbar_h = Scrollbar(interface, orient=HORIZONTAL, command=my_list_3.xview)
scrollbar_h.place(relx=0.6988, rely=0.583, width=320.5)

update(alist)

# output
# --> als waarde geselecteerd is, dan is je output het jaartal; hieronder test met knop, maar niet wat we moeten hebben. Hij moet als output de kolom langs de inputkolom geven
# https://sparkbyexamples.com/pandas/pandas-extract-column-value-based-on-another-column/ antwoord?
# if begindatum = empty, dan 'einddatum'; beide ingevuld dan beide geven

# output_begindatum = df.loc[df['GEBEURTENIS (PYTHON)'] == entry_1, 'Begindatum']


#df2 = df.loc[df['GEBEURTENIS (PYTHON)'] == [df['Begindatum']]]

#def output_3A(e):
 #   output_3.delete(0, END)
  #  output_3.insert(0, my_list_3.get(ACTIVE))

#https://www.datasciencemadesimple.com/append-concatenate-rows-python-pandas-row-bind/ --> als 'GEBR' = Begindatum ...? Eerst de
#koloms aan elkaar linken, dan moet dit mogelijk zijn?

#alist = df['GEBEURTENIS (PYTHON)'].tolist()
output = df['Begindatum'].tolist()

def waarden_Excel():
    df = df.apply(lambda alist: df['GEBEURTENIS (PYTHON)'] == df['Begindatum'])

def output_begindatum():
    if entry_1.get() == '':
    #if entry_1.get() == 'De muntenroute is zichtbaar':
        tekst = tk.Label(interface, text="goed")
        tekst.place(relx=0.3, rely=0.8)
    else:
        tekst = tk.Label(interface, text="dit komt niet voor in de lijst")
        tekst.place(relx=0.3, rely=0.8)


mijn_knop = Button(interface, text='klik hier', command=output_begindatum)
mijn_knop.place(relx=0.29, rely=0.7)

# OPTIE 3: op basis van fotograaf/handtekeningen/namen/personen
# OPTIE 4: overige (zoals kartelrand, KIK-nummer bv. B0...)
# KIK-nummer = "opgelet! Je geeft aan dat de foto een KIK-nummer bevat. Het originele beeld is dan ook terug te vinden in de database van het KIK. Kijk daar of de foto gedateerd is."
# Zowel één datering als overzicht + waarschuwing dat je altijd moet controleren

interface.mainloop()
