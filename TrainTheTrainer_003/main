import pandas as pd

df = pd.read_csv(r"C:\Users\decoseti\PycharmProjects\TtT03\Europeana_ttt.csv", delimiter=",")
#print(df)

# read kolomnamen
#print(df.columns)

#read 1 kolom
#print(df['object_name'][0:5])

#read meerdere kolommen
#print(df[['object_name','creator']])

#read 1 of meer rij(en)
#print(df.iloc[0:4])

#read een specifieke locatie
#komma: rij, kolom // combinatie is mogelijk [5:8, 3:9)
#print(df.iloc[5,3])

#wijzigen kolomnamen
#df = df.rename(columns={"object_name": "instellingsnaam"})

#deleten van kolom
#df3 = df.drop(["object_name"], 1)
#print(df3)

#kolom toevoegen
#df['Test'] = df['object_number'] + "_" + df['collection']
#print(df)

#verplaatsen van de kolom (bv. de laatste nieuwe naar voren verplaatsen)
# cols = list(df.columns.values)
# print(cols)
# df = df[cols[0:3] + [cols[-1]] + cols [4:26]]
# print(df)

#alfabetisch/numeriek sorteren (als je het oplopend wilt, geen ascending ingeven)
#df = df.sort_values('object_name', ascending=False)
#print(df)

#df4 = df.sort_values(['creator', 'material'], ascending=[0,2])
#print(df4)

#filteren
#df5 = df.loc[(df['production.place'] == 'Gent')]
#print(df5)

#filteren op meerdere zaken
#df6 = df.loc[(df['production.place'] == 'Gent') & (df['creator.role'] == 'ontwerper')]
#print(df6)

#opslaan als csv
#df6.to_csv('Gentseontwerpers.csv')

#waarden tellen
aantal_records = df["institution.name"].count()
print(aantal_records)

#aantal rcods vervaardigd in Gent (om een aantal te krijgen; nodig voor bv. grafieken)
#dus eigenlijk de records gaan tellen na het invoeren van een filter
#filterplaatsGent = df.loc[df['production.place'] == 'Gent']
#records_vervaardigdinGent = filterplaatsGent['production.place'].count()
#print(records_vervaardigdinGent)

#visualiseren met matplotlib
#from matplotlib import pyplot as plt
#vervaardigdinGent = [aantal_records-records_vervaardigdinGent, records_vervaardigdinGent]
#plt.pie(vervaardigdinGent)
#plt.show()