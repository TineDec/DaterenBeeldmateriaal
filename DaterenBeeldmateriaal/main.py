from tkinter import *
import tkinter as tk

interface = tk.Tk()
interface.configure(bg="#60c1c9")
# width x height + x_offset + y_offset:
interface.geometry("1200x700+30+30")

#kleurcode lichtblauw = #60c1c9
#kleurcode geel = #fdc20b
#kleurcode roze = #ea94aa
#kleurcode groen = #00a57e

titel = tk.Label(interface, text="DATEREN VAN BEELDMATERIAAL")
titel.configure(bg="#60c1c9", fg="#000000", font=("Calibri",20,"bold"), padx=500, pady=30)
titel.pack(fill=tk.X, expand=0)

#OPTIE 1: op basis van foto-techniek
#OPTIE 2: op basis van bezienswaardigheden
    #doorzoek thesaurus op vaste woorden

optie_2 = Label(interface, text = "Duid hier aan wat te zien is op de foto. Zoektermen moeten in het Nederlands en enkelvoud genoteerd worden.")
optie_2.configure(font=("Calibri",12), bg="#60c1c9", fg="#000000")
optie_2.place(x = 80, y = 100)

def thesaurus(event):
    keuzemenu = event.widget.get()
    print(keuzemenu)

    if keuzemenu == '':
        data = lijst
    else:
        data = []
        for item in lijst:
            if keuzemenu.lower() in item.lower():
                data.append(item)
    Update(data)

def Update(data):
    listbox.delete(0, 'end')
    #put new data
    for item in data:
        listbox.insert('end', item)

lijst = ('Tine', 'Saar', 'Flore')

entry = Entry(interface)
entry.pack()
entry.place(x = 80, y = 130, width=300, height=20)
entry.bind('<KeyRelease>', thesaurus)

entry_2 = Entry(interface)
entry_2.pack()
entry_2.place(x = 480, y = 130, width=300, height=20)
entry_2.bind('<KeyRelease>', thesaurus)

entry_3 = Entry(interface)
entry_3.pack()
entry_3.place(x = 880, y = 130, width=300, height=20)
entry_3.bind('<KeyRelease>', thesaurus)

listbox = Listbox(interface)
listbox.pack()
listbox.place(x = 80, y = 160, width=1100, height=100)
Update(lijst)
# --> KLIKBAAR maken (nu moet je de hele term overtypen, zorgen dat je kan klikken en zo naar het volgende kunt gaan)
    #5 opties om dan term aan te klikken
#OPTIE 3: op basis van fotograaf
#OPTIE 4: overige (zoals kartelrand)
#Zowel één datering als overzicht + waarschuwing dat je altijd moet controleren

interface.mainloop()