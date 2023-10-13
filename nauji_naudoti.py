from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# TIKSLAS: PALYGINTI, KIEK BUVO IS VISO REGISTRUOTA NAUJU IR
# NAUDOTU TRANSPORTO PRIEMONIU 2021 IR 2022 METAIS

# data_files = [('Files_csv/automobiliu_registracija_2021.csv', '2021'),
#               ('Files_csv/automobiliu_registracija_2022.csv', '2022')]
# plt.figure(figsize=(12, 8))
# bar_width = 0.35  # stulpelio plotis
# index = range(len(pd.read_csv(data_files[0][0], skipfooter=1, engine='python')['Menuo']))  # stulpelių indeksai
# for i, (data_file, year) in enumerate(data_files):
#     df = pd.read_csv(data_file, skipfooter=1, engine='python')
#     # Sukurti stulpelius naudotoms transporto priemonėms
#     plt.bar([ind + bar_width * i for ind in index], df['Is viso naudotu transporto priemoniu'],
#     width=bar_width, label=f'Naudoti {year}', alpha=0.7)
#     # Sukurti stulpelius naujoms transporto priemonėms
#     plt.bar([ind + bar_width * i for ind in index], df['Is viso nauju transporto priemoniu'],
#     width=bar_width, bottom=df['Is viso naudotu transporto priemoniu'], label=f'Nauji {year}', alpha=0.7)
# plt.xlabel('Menuo')
# plt.ylabel('Is viso registruota')
# plt.title('Transporto registracija 2021 vs 2022')
# plt.xticks([ind + bar_width / 2 for ind in index], df['Menuo'], rotation=45)
# plt.legend()
# plt.tight_layout()
# plt.show()

# ISVADA: ANALIZUOJANT PAMENESIUI MATYTI, KAD I LIETUVA IVEZAMA  BEVEIK TRIGUBAI DAUGIAU
# NAUDOTU, NEI NAUJU TRANSPORTO PRIEMONIU

# TIKSLAS: NUSTATYTI, KOKIA YRA NAUJU AUTOMOBILIU PROCENTINE DALIS
# NUO VISU REGISTRUOTU AUTOMOBILIU 2021/2022 METAIS
# STULPELINIS GRAFIKAS

# data_files = [('Files_csv/automobiliu_registracija_2021.csv', '2021'),
#               ('Files_csv/automobiliu_registracija_2022.csv', '2022')]
# procentai = []
# for data_file, year in data_files:
#     df = pd.read_csv(data_file, skipfooter=1, engine='python')
#     nauji = df['Is viso nauju transporto priemoniu'].sum()
#     viso = df['Is viso naudotu transporto priemoniu'].sum() + nauji
#     procentine_dalis = (nauji / viso) * 100
#     procentai.append(procentine_dalis)
#
# plt.bar([year for _, year in data_files], procentai, color=['blue', 'green'])
# plt.xlabel('Metai')
# plt.ylabel('Procentai')
# plt.title('Naujų automobilių procentinė dalis nuo viso registruotų automobilių')
# plt.ylim(0, 100)  # Nustatome Y ašies ribas nuo 0 iki 100
# plt.show()

# ISVADA: ANALIZUOJANT METINIUS DUOMENIS MATYTI, KAD I LIETUVA IVEZAMA  TIK TRECDALIS NAUJU TRANSPORTO
# PRIEMONIU NUO VISU PER METUS IVEZAMU TRANSPORTO PRIEMONIU
