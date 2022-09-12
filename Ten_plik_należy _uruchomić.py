import pandas as pd
from Pobieranie import Tworzenie_podwojnej_krotki

file=Tworzenie_podwojnej_krotki.Tworzenie_podwojnej_krotki()

L=[]
for i in file:
    L.append(pd.read_csv(i, encoding='ISO-8859-1', sep=';', header=0, index_col=None))

dataFrame = pd.concat(L, ignore_index=True)
dataFrame.to_csv('Polaczone.csv', sep=';', index=False)