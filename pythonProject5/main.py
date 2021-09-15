# 1. import matplotlib + pip install matplotlib
from matplotlib import pyplot as plt

# 2. Line Graphs

# Data invoegen
instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

# Grafiek maken
plt.plot(instellingen, aantal_records)

# Grafiek op scherm tonen
plt.show()

#######################################################################################################################

# x-y label toevoegen
instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.xlabel('CoGent Partners')
plt.ylabel('Aantal Ontsloten Records')

plt.plot(instellingen, aantal_records)
plt.show()

#######################################################################################################################

# titel toevoegen

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.xlabel('CoGent Partners')
plt.ylabel('Aantal Ontsloten Records')
plt.title("Aantal ontsloten Records/Instelling (CoGent)")

plt.plot(instellingen, aantal_records)
plt.show()

#######################################################################################################################

# stijl toevoegen: https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html
# beschikbare stijlen kunnen ook opgeroepen worden op terminal via: print(plt.style.available)

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.xlabel('CoGent Partners')
plt.ylabel('Aantal Ontsloten Records')
plt.title("Aantal ontsloten Records/Instelling (CoGent)")
plt.style.use("fivethirtyeight")

plt.plot(instellingen, aantal_records)
plt.show()

#######################################################################################################################

# zelf een kleur kiezen voor de lijn

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.style.use("default")
plt.xlabel('CoGent Partners')
plt.ylabel('Aantal Ontsloten Records')
plt.title("Aantal ontsloten Records/Instelling (CoGent)")

plt.plot(instellingen, aantal_records, color="#abcdef")
plt.show()

#######################################################################################################################

# lijnmarker kiezen (gestreept, gestipt, volle lijn)
# - : solid line (default)
# -- : dashed line style
# -. : dash-dot line style
# : : dotted line style

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.xlabel('CoGent Partners')
plt.ylabel('Aantal Ontsloten Records')
plt.title("Aantal ontsloten Records/Instelling (CoGent)")

plt.plot(instellingen, aantal_records, color="#abcdef", linestyle="--")
plt.show()

#######################################################################################################################

# lijnbreedte

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.xlabel('CoGent Partners')
plt.ylabel('Aantal Ontsloten Records')
plt.title("Aantal ontsloten Records/Instelling (CoGent)")

plt.plot(instellingen, aantal_records, color="#abcdef", linestyle="--", linewidth=10)
plt.show()

#######################################################################################################################

# grid toevoegen

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.xlabel('CoGent Partners')
plt.ylabel('Aantal Ontsloten Records')
plt.title("Aantal ontsloten Records/Instelling (CoGent)")
plt.grid(True)

plt.plot(instellingen, aantal_records, color="#abcdef", linestyle="--", linewidth=10)
plt.show()

#######################################################################################################################

# Aantal records per instelling doorheen de tijd

maanden = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus']
aantal_records_IM = [1451, 2314, 2846, 3123, 3845, 3975, 4578, 5422]

plt.xlabel('months')
plt.ylabel('aantal records')
plt.title("Aantal ontsloten Records/maand (IM)")
plt.grid(True)

plt.plot(maanden, aantal_records_IM)
plt.show()

#######################################################################################################################

# meerdere lijnen op een grafiek

maanden = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus']
aantal_records_IM = [1451, 2314, 2846, 3123, 3845, 3975, 4578, 5422]
aantal_records_DMG = [845, 1564, 1846, 2684, 3123, 3975, 4123, 4415]
aantal_records_HVA = [584, 1651, 1845, 2123, 2845, 2965, 3546, 3846]
aantal_records_STAM = [1512, 1845, 2856, 3545, 4546, 4845, 5456, 6541]
aantal_records_ARCHIEF = [1845, 2314, 2894, 3648, 4546, 5123, 5846, 6154]

plt.xlabel('months')
plt.ylabel('aantal records')
plt.title("Aantal ontsloten Records/maand (IM)")
plt.grid(True)

plt.plot(maanden, aantal_records_IM)
plt.plot(maanden, aantal_records_DMG)
plt.plot(maanden, aantal_records_HVA)
plt.plot(maanden, aantal_records_STAM)
plt.plot(maanden, aantal_records_ARCHIEF)

plt.show()

#######################################################################################################################

# meerdere lijnen op een grafiek

maanden = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus']
aantal_records_IM = [1451, 2314, 2846, 3123, 3845, 3975, 4578, 5422]
aantal_records_DMG = [845, 1564, 1846, 2684, 3123, 3975, 4123, 4415]
aantal_records_HVA = [584, 1651, 1845, 2123, 2845, 2965, 3546, 3846]
aantal_records_STAM = [1512, 1845, 2856, 3545, 4546, 4845, 5456, 6541]
aantal_records_ARCHIEF = [1845, 2314, 2894, 3648, 4546, 5123, 5846, 6154]

plt.xlabel('months')
plt.ylabel('aantal records')
plt.title("Aantal ontsloten Records/maand (IM)")
plt.grid(True)

plt.plot(maanden, aantal_records_IM)
plt.plot(maanden, aantal_records_DMG)
plt.plot(maanden, aantal_records_HVA)
plt.plot(maanden, aantal_records_STAM)
plt.plot(maanden, aantal_records_ARCHIEF)

plt.show()

#######################################################################################################################

# legende toevoegen

maanden = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus']
aantal_records_IM = [1451, 2314, 2846, 3123, 3845, 3975, 4578, 5422]
aantal_records_DMG = [845, 1564, 1846, 2684, 3123, 3975, 4123, 4415]
aantal_records_HVA = [584, 1651, 1845, 2123, 2845, 2965, 3546, 3846]
aantal_records_STAM = [1512, 1845, 2856, 3545, 4546, 4845, 5456, 6541]
aantal_records_ARCHIEF = [1845, 2314, 2894, 3648, 4546, 5123, 5846, 6154]

plt.xlabel('months')
plt.ylabel('aantal records')
plt.title("Aantal ontsloten Records/maand (IM)")
plt.grid(True)

plt.plot(maanden, aantal_records_IM)
plt.plot(maanden, aantal_records_DMG)
plt.plot(maanden, aantal_records_HVA)
plt.plot(maanden, aantal_records_STAM)
plt.plot(maanden, aantal_records_ARCHIEF)

plt.legend(["IM", 'DMG', 'HVA', 'STAM', 'ARCHIEF'])
plt.show()

#######################################################################################################################

# 2. Bar Graphs

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.xlabel('CoGent Partners')
plt.ylabel('Aantal Ontsloten Records')
plt.title("Aantal ontsloten Records/Instelling (CoGent)")

plt.bar(instellingen, aantal_records, color="#abcdef")
plt.show()

#######################################################################################################################

# Kleuren kiezen voor elke bar

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.xlabel('CoGent Partners')
plt.ylabel('Aantal Ontsloten Records')
plt.title("Aantal ontsloten Records/Instelling (CoGent)")
colors = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']

plt.bar(instellingen, aantal_records, color=colors)
plt.show()

#######################################################################################################################

# horizontale bar chart

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.ylabel('CoGent Partners')
plt.xlabel('Aantal Ontsloten Records')
plt.title("Aantal ontsloten Records/Instelling (CoGent)")
colors = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']

plt.barh(instellingen, aantal_records, color=colors)
plt.show()

#######################################################################################################################

# Breedte van de bars

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.xlabel('CoGent Partners')
plt.ylabel('Aantal Ontsloten Records')
plt.title("Aantal ontsloten Records/Instelling (CoGent)")
colors = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']

plt.bar(instellingen, aantal_records, color=colors, width=0.4)
plt.show()

#######################################################################################################################

# meerdere waarden per bar

maanden = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus']
aantal_records_IM = [1451, 2314, 2846, 3123, 3845, 3975, 4578, 5422]
aantal_records_DMG = [845, 1564, 1846, 2684, 3123, 3975, 4123, 4415]

plt.bar(maanden, aantal_records_IM)
plt.bar(maanden, aantal_records_DMG, bottom=aantal_records_IM)

plt.show()

#######################################################################################################################

# 3. Pie Charts

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.pie(aantal_records)
plt.show()

#######################################################################################################################

# add labels

# instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.pie(aantal_records, labels=instellingen)
plt.show()

#######################################################################################################################

# add percentage

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]

plt.pie(aantal_records, labels=instellingen, autopct='%1.1f%%')
plt.show()

#######################################################################################################################

# add colors

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]
kleuren = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']

plt.pie(aantal_records, labels=instellingen, autopct='%1.1f%%', colors=kleuren)
plt.show()

#######################################################################################################################

# startangle

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]
kleuren = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']

plt.pie(aantal_records, labels=instellingen, autopct='%1.1f%%', colors=kleuren, startangle=90)
plt.show()

#######################################################################################################################

# explode piepiece

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]
kleuren = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']
explode = [0, 0, 0.1, 0, 0]

plt.pie(aantal_records, labels=instellingen, autopct='%1.1f%%', colors=kleuren, startangle=90, explode=explode)
plt.show()

#######################################################################################################################

# add shadow

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]
kleuren = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']
explode = [0, 0, 0.1, 0, 0]

plt.pie(aantal_records, labels=instellingen, autopct='%1.1f%%', colors=kleuren, startangle=90, explode=explode,
        shadow=True)
plt.show()

#######################################################################################################################

# comic style

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]
kleuren = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']
explode = [0, 0, 0.1, 0, 0]

plt.xkcd()
plt.pie(aantal_records, labels=instellingen, autopct='%1.1f%%', colors=kleuren, startangle=90, explode=explode,
        shadow=True)
plt.show()

#######################################################################################################################

# save graphs

instellingen = ['IM', 'STAM', 'HvA', 'DMG', 'Archief']
aantal_records = [5422, 6541, 3846, 4451, 6154]
kleuren = ['#abcdef', '#aabbcc', '#ddeeff', "#aaccdd", '#bbddee']
explode = [0, 0, 0.1, 0, 0]

plt.xkcd()
plt.pie(aantal_records, labels=instellingen, autopct='%1.1f%%', colors=kleuren, startangle=90, explode=explode,
        shadow=True)
plt.savefig("ontslotenrecords.jpg")
plt.show()