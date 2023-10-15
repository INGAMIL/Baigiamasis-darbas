from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# TIKSLAS: PATIKRINTI, AR EGZISTUOJA AUTOMOBILIU PIRKIMO SEZONISKUMAS: 2021/2022

# atliekame duomenu automobiliu_registracija_2021 ir automobiliu_registracija 2022 apdorojima, kad issiaiskintume,
# kokiais 5 menesiais ivezama daugiausia automobiliu is viso ir kiek M1 klases automobiliu.

# suminiai_duomenys_2021 = pd.read_csv('Files_csv/automobiliu_registracija_2021.csv', skipfooter=1, engine='python')
# suminiai_duomenys_2021['suma_transporto_priemoniu_2021'] = suminiai_duomenys_2021['Is viso naudotu transporto priemoniu']
# +suminiai_duomenys_2021['Is viso nauju transporto priemoniu']
# top_5_menesiai_is_viso_transporto_2021 =suminiai_duomenys_2021.nlargest(5, 'suma_transporto_priemoniu_2021')
# [['Menuo', 'suma_transporto_priemoniu_2021']]
# print(top_5_menesiai_is_viso_transporto_2021.to_string(index=False))
#
# suminiai_duomenys_2021['suma_M1_klases_2021'] = suminiai_duomenys_2021['Is ju M1 klases naudotu lengvuju automobiliu']
# +suminiai_duomenys_2021['Is ju M1 klases nauju lengvuju automobiliu']
# top_5_menesiai_is_viso_M1_2021 = suminiai_duomenys_2021.nlargest(5, 'suma_M1_klases_2021')
# [['Menuo', 'suma_M1_klases_2021']]
# print(top_5_menesiai_is_viso_M1_2021.to_string(index=False))
# #
# suminiai_duomenys_2022 = pd.read_csv('Files_csv/automobiliu_registracija_2022.csv', skipfooter=1, engine='python')
# suminiai_duomenys_2022['suma_transporto_priemoniu_2022'] = suminiai_duomenys_2022['Is viso naudotu transporto priemoniu']
# +suminiai_duomenys_2022['Is viso nauju transporto priemoniu']
# top_5_menesiai_is_viso_transporto_2022 =suminiai_duomenys_2022.nlargest(5, 'suma_transporto_priemoniu_2022')
# [['Menuo', 'suma_transporto_priemoniu_2022']]
# print(top_5_menesiai_is_viso_transporto_2022.to_string(index=False))
#
# suminiai_duomenys_2022['suma_M1_klases_2022'] = suminiai_duomenys_2022['Is ju M1 klases naudotu lengvuju automobiliu']
# +suminiai_duomenys_2022['Is ju M1 klases nauju lengvuju automobiliu']
# top_5_menesiai_is_viso_M1_2022 = suminiai_duomenys_2022.nlargest(5, 'suma_M1_klases_2022')
# [['Menuo', 'suma_M1_klases_2022']]
# print(top_5_menesiai_is_viso_M1_2022.to_string(index=False))
#
# plt.figure(figsize=(14, 10))
# # # Viso transporto priemonių 2021
# plt.subplot(2, 2, 1)
# plt.bar(top_5_menesiai_is_viso_transporto_2021['Menuo'],
# top_5_menesiai_is_viso_transporto_2021['suma_transporto_priemoniu_2021'], color='blue', label='2021')
# plt.title('Top 5 mėnesiai pagal viso transporto priemonių skaičių 2021')
# plt.xlabel('Mėnuo')
# plt.ylabel('Kiekis')
# plt.xticks(rotation=45)
# # # M1 klasės lengvųjų automobilių 2021
# plt.subplot(2, 2, 2)
# plt.bar(top_5_menesiai_is_viso_M1_2021['Menuo'],
# top_5_menesiai_is_viso_M1_2021['suma_M1_klases_2021'], color='green', label='2021')
# plt.title('Top 5 mėnesiai pagal M1 klasės lengvųjų automobilių skaičių 2021')
# plt.xlabel('Mėnuo')
# plt.ylabel('Kiekis')
# plt.xticks(rotation=45)
# # Viso transporto priemonių 2022
# plt.subplot(2, 2, 3)
# plt.bar(top_5_menesiai_is_viso_transporto_2022['Menuo'],
# top_5_menesiai_is_viso_transporto_2022['suma_transporto_priemoniu_2022'], color='blue', label='2022')
# plt.title('Top 5 mėnesiai pagal viso transporto priemonių skaičių 2022')
# plt.xlabel('Mėnuo')
# plt.ylabel('Kiekis')
# plt.xticks(rotation=45)
# # # M1 klasės lengvųjų automobilių 2022
# plt.subplot(2, 2, 4)
# plt.bar(top_5_menesiai_is_viso_M1_2022['Menuo'],
# top_5_menesiai_is_viso_M1_2022['suma_M1_klases_2022'], color='green', label='2022')
# plt.title('Top 5 mėnesiai pagal M1 klasės lengvųjų automobilių skaičių 2022')
# plt.xlabel('Mėnuo')
# plt.ylabel('Kiekis')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig('Grafikai/suminis_top5_menesiai_2021_2022.jpg')
# plt.show()

# 3 menesiai, per kuriuos i Lietuva ivezama maziausiai transporto priemoniu:

suminiai_duomenys_2021 = pd.read_csv('Files_csv/automobiliu_registracija_2021.csv', skipfooter=1, engine='python')
suminiai_duomenys_2021['suma_transporto_priemoniu_2021'] = suminiai_duomenys_2021['Is viso naudotu transporto priemoniu']
+suminiai_duomenys_2021['Is viso nauju transporto priemoniu']
low_3_menesiai_is_viso_transporto_2021 =suminiai_duomenys_2021.nsmallest(3, 'suma_transporto_priemoniu_2021')
[['Menuo', 'suma_transporto_priemoniu_2021']]
print(low_3_menesiai_is_viso_transporto_2021.to_string(index=False))

suminiai_duomenys_2021['suma_M1_klases_2021'] = suminiai_duomenys_2021['Is ju M1 klases naudotu lengvuju automobiliu']
+suminiai_duomenys_2021['Is ju M1 klases nauju lengvuju automobiliu']
low_3_menesiai_is_viso_M1_2021 = suminiai_duomenys_2021.nsmallest(3, 'suma_M1_klases_2021')[['Menuo', 'suma_M1_klases_2021']]
print(low_3_menesiai_is_viso_M1_2021.to_string(index=False))

#
suminiai_duomenys_2022 = pd.read_csv('Files_csv/automobiliu_registracija_2022.csv', skipfooter=1, engine='python')
suminiai_duomenys_2022['suma_transporto_priemoniu_2022'] = suminiai_duomenys_2022['Is viso naudotu transporto priemoniu']
+suminiai_duomenys_2022['Is viso nauju transporto priemoniu']
low_3_menesiai_is_viso_transporto_2022 =suminiai_duomenys_2022.nsmallest(3, 'suma_transporto_priemoniu_2022')
[['Menuo', 'suma_transporto_priemoniu_2022']]
print(low_3_menesiai_is_viso_transporto_2022.to_string(index=False))
#
suminiai_duomenys_2022['suma_M1_klases_2022'] = suminiai_duomenys_2022['Is ju M1 klases naudotu lengvuju automobiliu']
+suminiai_duomenys_2022['Is ju M1 klases nauju lengvuju automobiliu']
low_3_menesiai_is_viso_M1_2022 = suminiai_duomenys_2022.nsmallest(3, 'suma_M1_klases_2022')
[['Menuo', 'suma_M1_klases_2022']]
print(low_3_menesiai_is_viso_M1_2022.to_string(index=False))

plt.figure(figsize=(14, 10))
# # Viso transporto priemonių 2021
plt.subplot(2, 2, 1)
plt.bar(low_3_menesiai_is_viso_transporto_2021['Menuo'],
low_3_menesiai_is_viso_transporto_2021['suma_transporto_priemoniu_2021'], color='blue', label='2021')
plt.title('Mažiausiai įvežama is viso transporto priemonių 2021')
plt.xlabel('Mėnuo')
plt.ylabel('Kiekis')
plt.xticks(rotation=45)
# M1 klasės lengvųjų automobilių 2021
plt.subplot(2, 2, 2)
plt.bar(low_3_menesiai_is_viso_M1_2021['Menuo'],
low_3_menesiai_is_viso_M1_2021['suma_M1_klases_2021'], color='green', label='2021')
plt.title('Mažiausiai įvežama M1 klasės lengvųjų automobilių 2021')
plt.xlabel('Mėnuo')
plt.ylabel('Kiekis')
plt.xticks(rotation=45)
# # Viso transporto priemonių 2022
plt.subplot(2, 2, 3)
plt.bar(low_3_menesiai_is_viso_transporto_2022['Menuo'],
low_3_menesiai_is_viso_transporto_2022['suma_transporto_priemoniu_2022'], color='blue', label='2022')
plt.title('Mažiausiai įvežama iš viso transporto priemonių 2022')
plt.xlabel('Mėnuo')
plt.ylabel('Kiekis')
plt.xticks(rotation=45)
# # M1 klasės lengvųjų automobilių 2022
plt.subplot(2, 2, 4)
plt.bar(low_3_menesiai_is_viso_M1_2022['Menuo'],
low_3_menesiai_is_viso_M1_2022['suma_M1_klases_2022'], color='green', label='2022')
plt.title('Mažiausiai įvežama M1 klasės lengvųjų automobilių 2022')
plt.xlabel('Mėnuo')
plt.ylabel('Kiekis')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Grafikai/suminis_low3_menesiai_2021_2022.jpg')
plt.show()

# ISVADA: LIETUVOJE DOMINUOJA I LIETUVA IVEZAMU PIRMA KARTA AUTOMOBILIU SEZONISKUMAS:
# DAUGIAUSIAI AUTOMOBILIU REGISTRACIJU ATLIEKAMA PAVASARI IR VASAROS PRADZIOJE.
# Paanalizavus duomenis, matome, kad yra tam tikri mėnesiai, kada daugiausia įregistruojama transporto priemonių.
# Šie mėnesiai gali būti susiję su automobilių pardavimo akcijomis, naujų modelių pristatymu
# ar kitais sezoniniais veiksniais: pvz. daugiau motociklu ir mopedu ivezama balandzio- birzelio men.
# 3 POPULIARIAUSI MENESIAI YRA:BALANDIS/GEGUZE/BIRZELIS
# 3 MENESIAI, KUOMET MAZIAUSIAI IVEZAMA YRA:SAUSIS/VASARIS/GRUODIS

#  STULPELINIS GRAFIKAS:
#
# data_files = [('Files_csv/automobiliu_registracija_2021.csv', '2021'),
#               ('Files_csv/automobiliu_registracija_2022.csv', '2022')]
# plt.figure(figsize=(12, 8))
# # # Nustatome stulpelių plotį ir jų tarpą
# bar_width = 0.35
# index = range(len(pd.read_csv(data_files[0][0], skipfooter=1, engine='python')['Menuo']))
# bars = []
# for i, (data_file, year) in enumerate(data_files):
#     df = pd.read_csv(data_file, skipfooter=1, engine='python')
#     df['Is viso registruota'] = df['Is viso naudotu transporto priemoniu'] + df['Is viso nauju transporto priemoniu']
#     bars.append(plt.bar([ind + bar_width * i for ind in index], df['Is viso registruota'], bar_width, label=f'{year}'))
# plt.xlabel('Menuo')
# plt.ylabel('Is viso registruota')
# plt.title('Transporto registracija 2021 vs 2022')
# plt.xticks([ind + bar_width for ind in index], df['Menuo'], rotation=45)
# plt.legend()
# plt.tight_layout()
# plt.savefig('Grafikai/Transporto_registracija_2021_vs_2022_stulpelinis.jpg')
# plt.show()

# ISVADA: PALYGINUS 2021-2022 METUS, MATYTI, KAD REGISTRUOJAMU AUTOMOBILIU SEZONISKUMO TENDENCIJA
# ISLIEKA PANASI.

 # LINIJINIS GRAFIKAS:

# data_files = [('Files_csv/automobiliu_registracija_2021.csv', '2021'),
#               ('Files_csv/automobiliu_registracija_2022.csv', '2022')]
# plt.figure(figsize=(12, 8))
# for data_file, year in data_files:
#     df = pd.read_csv(data_file, skipfooter=1, engine='python')
#     df['Is viso registruota'] = df['Is viso naudotu transporto priemoniu'] + df['Is viso nauju transporto priemoniu']
#     plt.plot(df['Menuo'], df['Is viso registruota'], marker='o', label=f'{year}')
# plt.xlabel('Menuo')
# plt.ylabel('Is viso registruota')
# plt.title('Transporto registracija 2021 vs 2022')
# plt.xticks(rotation=45)
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # pridedame tinklelį grafičiui
# plt.legend()
# plt.tight_layout()
# plt.savefig('Grafikai/Transporto_registracija_2021_vs_2022_linijinis_jpg')
# plt.show()

# DVIEJU METU DUOMENYS STULPELINIUOSE GRAFIKUOSE ATVAIZDUOJAMI VIENAME LAPE:

# data_files = [('Files_csv/automobiliu_registracija_2021.csv', '2021'),
#               ('Files_csv/automobiliu_registracija_2022.csv', '2022')]
# plt.figure(figsize=(12, 8))
# for index, (data_file, year) in enumerate(data_files, 1):
#     df = pd.read_csv(data_file, skipfooter=1, engine='python')
#     df['Is viso registruota'] = df['Is viso naudotu transporto priemoniu'] + df['Is viso nauju transporto priemoniu']
#     naujas_df = df[['Menuo', 'Is viso registruota']].copy()
#     plt.subplot(2, 1, index)
#     plt.bar(naujas_df['Menuo'], naujas_df['Is viso registruota'])
#     plt.xlabel('Menuo')
#     plt.ylabel('Is viso registruota')
#     plt.title(f'Transporto registracija {year}')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
# plt.savefig('Grafikai/Transporto_registracija_2021_2022_suminis_stulpelinis.jpg')
# plt.show()
# ISVADA: VIZUALIZACIJAI IR 2021/2022 METU PALYGINIMUI TINKAMAS IR STULPELINIS, IR LINIJINIS GRAFIKAS.
