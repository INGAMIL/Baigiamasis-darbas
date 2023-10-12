from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np



# is viso registracijos lentele 2021- 2022
# url = 'https://www.regitra.lt/lt/atviri-duomenys/?datayear=2021&dataquery='
# response = requests.get(url)
# # print(response.status_code)
# soup = BeautifulSoup(response.content, 'html.parser')
# table = soup.find('table', class_='grey large left')
# print(table)
# data = []
# if table:
#
#     rows = table.find_all('tr')
#
#     for row in rows[1:14]:
#         columns = row.find_all('td')
#         if len(columns)>=5:
#             Menuo = columns[0].text.strip()
#             Is_viso_naudotu_transporto_priemoniu = columns[1].text.strip()
#             Is_ju_M1_klases_naudotu_lengvuju_automobiliu = columns[2].text.strip()
#             Is_viso_nauju_transporto_priemoniu = columns[3].text.strip()
#             Is_ju_M1_klases_nauju_lengvuju_automobiliu = columns[4].text.strip()
#
#         data.append({
#             'Menuo': Menuo,
#             'Is viso naudotu transporto priemoniu': Is_viso_naudotu_transporto_priemoniu,
#             'Is ju M1 klases naudotu lengvuju automobiliu': Is_ju_M1_klases_naudotu_lengvuju_automobiliu,
#             'Is viso nauju transporto priemoniu': Is_viso_nauju_transporto_priemoniu,
#             'Is ju M1 klases nauju lengvuju automobiliu': Is_ju_M1_klases_nauju_lengvuju_automobiliu,
#         })
# column_names = ['Menuo', 'Is viso naudotu transporto priemoniu', 'Is ju M1 klases naudotu lengvuju automobiliu',
#                         'Is viso nauju transporto priemoniu', 'Is ju M1 klases nauju lengvuju automobiliu']
# df = pd.DataFrame(data, columns=column_names)
# print(df)
#
# df.to_csv('automobiliu_registracija_2021.csv')

# url = 'https://www.regitra.lt/lt/atviri-duomenys/?datayear=2022&dataquery='
# response = requests.get(url)
# # print(response.status_code)
# soup = BeautifulSoup(response.content, 'html.parser')
# table = soup.find('table', class_='grey large left')
# print(table)
# data = []
# if table:
#
#     rows = table.find_all('tr')
#
#     for row in rows[1:14]:
#         columns = row.find_all('td')
#         if len(columns)>=5:
#             Menuo = columns[0].text.strip()
#             Is_viso_naudotu_transporto_priemoniu = columns[1].text.strip()
#             Is_ju_M1_klases_naudotu_lengvuju_automobiliu = columns[2].text.strip()
#             Is_viso_nauju_transporto_priemoniu = columns[3].text.strip()
#             Is_ju_M1_klases_nauju_lengvuju_automobiliu = columns[4].text.strip()
#
#         data.append({
#             'Menuo': Menuo,
#             'Is viso naudotu transporto priemoniu': Is_viso_naudotu_transporto_priemoniu,
#             'Is ju M1 klases naudotu lengvuju automobiliu': Is_ju_M1_klases_naudotu_lengvuju_automobiliu,
#             'Is viso nauju transporto priemoniu': Is_viso_nauju_transporto_priemoniu,
#             'Is ju M1 klases nauju lengvuju automobiliu': Is_ju_M1_klases_nauju_lengvuju_automobiliu,
#         })
# column_names = ['Menuo', 'Is viso naudotu transporto priemoniu', 'Is ju M1 klases naudotu lengvuju automobiliu',
#                         'Is viso nauju transporto priemoniu', 'Is ju M1 klases nauju lengvuju automobiliu']
# df = pd.DataFrame(data, columns=column_names)
# print(df)

# df.to_csv('automobiliu_registracija_2022.csv')

# ANALIZE
# 2021 METAI IVEZTU I LT IS VISO:

# df = pd.read_csv('Files_csv/automobiliu_registracija_2021.csv', skipfooter=1, engine='python')
# df['Is viso registruota'] = df['Is viso naudotu transporto priemoniu']+df['Is viso nauju transporto priemoniu']
# naujas_df_2021 = df[['Menuo', 'Is viso registruota']].copy()
# print(naujas_df_2021)
#
# plt.figure(figsize=(10,6))
# plt.bar(naujas_df_2021['Menuo'], naujas_df_2021['Is viso registruota'])
# plt.xlabel('Menuo')
# plt.ylabel('Is viso registruota')
# plt.title('Transporto registracija 2021')
# plt.xticks(rotation=45)
# plt.show()

df = pd.read_csv('Files_csv/automobiliu_registracija_2022.csv', skipfooter=1, engine='python')
df['Is viso registruota'] = df['Is viso naudotu transporto priemoniu']+df['Is viso nauju transporto priemoniu']
naujas_df_2022 = df[['Menuo', 'Is viso registruota']].copy()
print(naujas_df_2022)
plt.figure(figsize=(10,6))
plt.bar(naujas_df_2022['Menuo'], naujas_df_2022['Is viso registruota'])
plt.xlabel('Menuo')
plt.ylabel('Is viso registruota')
plt.title('Transporto registracija 2022')
plt.xticks(rotation=45)
plt.show()

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
#
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
# # Viso transporto priemonių 2021
# plt.subplot(2, 2, 1)
# plt.bar(top_5_menesiai_is_viso_transporto_2021['Menuo'],
# top_5_menesiai_is_viso_transporto_2021['suma_transporto_priemoniu_2021'], color='blue', label='2021')
# plt.title('Top 5 mėnesiai pagal viso transporto priemonių skaičių 2021')
# plt.xlabel('Mėnuo')
# plt.ylabel('Kiekis')
# plt.xticks(rotation=45)
# # M1 klasės lengvųjų automobilių 2021
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
# # M1 klasės lengvųjų automobilių 2022
# plt.subplot(2, 2, 4)
# plt.bar(top_5_menesiai_is_viso_M1_2022['Menuo'],
# top_5_menesiai_is_viso_M1_2022['suma_M1_klases_2022'], color='green', label='2022')
# plt.title('Top 5 mėnesiai pagal M1 klasės lengvųjų automobilių skaičių 2022')
# plt.xlabel('Mėnuo')
# plt.ylabel('Kiekis')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# 3 menesiai, per kuriuos i Lietuva ivezama maziausiai transporto priemoniu:

# suminiai_duomenys_2021 = pd.read_csv('Files_csv/automobiliu_registracija_2021.csv', skipfooter=1, engine='python')
# suminiai_duomenys_2021['suma_transporto_priemoniu_2021'] = suminiai_duomenys_2021['Is viso naudotu transporto priemoniu']
# +suminiai_duomenys_2021['Is viso nauju transporto priemoniu']
# low_3_menesiai_is_viso_transporto_2021 =suminiai_duomenys_2021.nsmallest(3, 'suma_transporto_priemoniu_2021')
# [['Menuo', 'suma_transporto_priemoniu_2021']]
# print(low_3_menesiai_is_viso_transporto_2021.to_string(index=False))
#
# suminiai_duomenys_2021['suma_M1_klases_2021'] = suminiai_duomenys_2021['Is ju M1 klases naudotu lengvuju automobiliu']
# +suminiai_duomenys_2021['Is ju M1 klases nauju lengvuju automobiliu']
# low_3_menesiai_is_viso_M1_2021 = suminiai_duomenys_2021.nsmallest(3, 'suma_M1_klases_2021')[['Menuo', 'suma_M1_klases_2021']]
# print(low_3_menesiai_is_viso_M1_2021.to_string(index=False))
#
#
# suminiai_duomenys_2022 = pd.read_csv('Files_csv/automobiliu_registracija_2022.csv', skipfooter=1, engine='python')
# suminiai_duomenys_2022['suma_transporto_priemoniu_2022'] = suminiai_duomenys_2022['Is viso naudotu transporto priemoniu']
# +suminiai_duomenys_2022['Is viso nauju transporto priemoniu']
# low_3_menesiai_is_viso_transporto_2022 =suminiai_duomenys_2022.nsmallest(3, 'suma_transporto_priemoniu_2022')
# [['Menuo', 'suma_transporto_priemoniu_2022']]
# print(low_3_menesiai_is_viso_transporto_2022.to_string(index=False))
#
# suminiai_duomenys_2022['suma_M1_klases_2022'] = suminiai_duomenys_2022['Is ju M1 klases naudotu lengvuju automobiliu']
# +suminiai_duomenys_2022['Is ju M1 klases nauju lengvuju automobiliu']
# low_3_menesiai_is_viso_M1_2022 = suminiai_duomenys_2022.nsmallest(3, 'suma_M1_klases_2022')
# [['Menuo', 'suma_M1_klases_2022']]
# print(low_3_menesiai_is_viso_M1_2022.to_string(index=False))
#
# plt.figure(figsize=(14, 10))
# # Viso transporto priemonių 2021
# plt.subplot(2, 2, 1)
# plt.bar(low_3_menesiai_is_viso_transporto_2021['Menuo'],
# low_3_menesiai_is_viso_transporto_2021['suma_transporto_priemoniu_2021'], color='blue', label='2021')
# plt.title('Maziausiai ivezama is viso transporto priemonių skaičių 2021')
# plt.xlabel('Mėnuo')
# plt.ylabel('Kiekis')
# plt.xticks(rotation=45)
# # M1 klasės lengvųjų automobilių 2021
# plt.subplot(2, 2, 2)
# plt.bar(low_3_menesiai_is_viso_M1_2021['Menuo'],
# low_3_menesiai_is_viso_M1_2021['suma_M1_klases_2021'], color='green', label='2021')
# plt.title('Maziausiai ivezama M1 klasės lengvųjų automobilių skaičių 2021')
# plt.xlabel('Mėnuo')
# plt.ylabel('Kiekis')
# plt.xticks(rotation=45)
# # Viso transporto priemonių 2022
# plt.subplot(2, 2, 3)
# plt.bar(low_3_menesiai_is_viso_transporto_2022['Menuo'],
# low_3_menesiai_is_viso_transporto_2022['suma_transporto_priemoniu_2022'], color='blue', label='2022')
# plt.title('Maziausiai ivezama is viso transporto priemonių skaičių 2022')
# plt.xlabel('Mėnuo')
# plt.ylabel('Kiekis')
# plt.xticks(rotation=45)
# # M1 klasės lengvųjų automobilių 2022
# plt.subplot(2, 2, 4)
# plt.bar(low_3_menesiai_is_viso_M1_2022['Menuo'],
# low_3_menesiai_is_viso_M1_2022['suma_M1_klases_2022'], color='green', label='2022')
# plt.title('Maziausiai ivezama M1 klasės lengvųjų automobilių skaičių 2022')
# plt.xlabel('Mėnuo')
# plt.ylabel('Kiekis')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# ISVADA: LIETUVOJE DOMINUOJA I LIETUVA IVEZAMU PIRMA KARTA AUTOMOBILIU SEZONISKUMAS:
# DAUGIAUSIAI AUTOMOBILIU REGISTRACIJU ATLIEKAMA PAVASARI IR VASAROS PRADZIOJE.
# Paanalizavus duomenis, matome, kad yra tam tikri mėnesiai, kada daugiausia įregistruojama transporto priemonių.
# Šie mėnesiai gali būti susiję su automobilių pardavimo akcijomis, naujų modelių pristatymu
# ar kitais sezoniniais veiksniais: pvz. daugiau motociklu ir mopedu ivezama balandzio- birzelio men.
# 3 POPULIARIAUSI MENESIAI YRA:BALANDIS/GEGUZE/BIRZELIS
# 3 MENESIAI, KUOMET MAZIAUSIAI IVEZAMA YRA:SAUSIS/VASARIS/GRUODIS

#  STULPELINIS GRAFIKAS:

# data_files = [('Files_csv/automobiliu_registracija_2021.csv', '2021'),
#               ('Files_csv/automobiliu_registracija_2022.csv', '2022')]
# plt.figure(figsize=(12, 8))
# # Nustatome stulpelių plotį ir jų tarpą
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
# plt.show()
# ISVADA: VIZUALIZACIJAI IR 2021/2022 METU PALYGINIMUI TINKAMAS IR STULPELINIS, IR LINIJINIS GRAFIKAS.


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

data_files = [('Files_csv/automobiliu_registracija_2021.csv', '2021'),
              ('Files_csv/automobiliu_registracija_2022.csv', '2022')]
procentai = []
for data_file, year in data_files:
    df = pd.read_csv(data_file, skipfooter=1, engine='python')
    nauji = df['Is viso nauju transporto priemoniu'].sum()
    viso = df['Is viso naudotu transporto priemoniu'].sum() + nauji
    procentine_dalis = (nauji / viso) * 100
    procentai.append(procentine_dalis)

plt.bar([year for _, year in data_files], procentai, color=['blue', 'green'])
plt.xlabel('Metai')
plt.ylabel('Procentai')
plt.title('Naujų automobilių procentinė dalis nuo viso registruotų automobilių')
plt.ylim(0, 100)  # Nustatome Y ašies ribas nuo 0 iki 100
plt.show()

# ISVADA: ANALIZUOJANT METINIUS DUOMENIS MATYTI, KAD I LIETUVA IVEZAMA  TIK TRECDALIS NAUJU TRANSPORTO
# PRIEMONIU NUO VISU PER METUS IVEZAMU TRANSPORTO PRIEMONIU


# TIKSLAS: NUSTATYTI, KOKIOS TRANSPORTO PRIEMONIU MARKES YRA POPULIARIAUSIOS LIETUVOJE.

# NAUJU IR NAUDOTU AUTOMOBILIU POPULIARUMO LENTELES:

# url = 'https://www.regitra.lt/lt/atviri-duomenys/?datayear=2022&dataquery='
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# tables = soup.find_all('table', class_='grey large left')
# if len(tables) >= 2:
#     data1 = []
#     data2 = []
#     # Pirmoji lentelė
#     rows = tables[1].find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         if len(columns) >= 6:
#             data1.append({
#                 'Mėnuo': columns[0].text.strip(),
#                 'TOYOTA': columns[1].text.strip(),
#                 'VOLKSWAGEN': columns[2].text.strip(),
#                 'SKODA': columns[3].text.strip(),
#                 'KIA': columns[4].text.strip(),
#                 'NISSAN': columns[5].text.strip()
#             })
#     # Antroji lentelė
#     rows = tables[2].find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         if len(columns) >= 6:
#             data2.append({
#                 'Mėnuo': columns[0].text.strip(),
#                 'VOLKSWAGEN': columns[1].text.strip(),
#                 'BMW': columns[2].text.strip(),
#                 'AUDI': columns[3].text.strip(),
#                 'TOYOTA': columns[4].text.strip(),
#                 'OPEL': columns[5].text.strip()
#             })
#     df1 = pd.DataFrame(data1, columns=['Mėnuo', 'TOYOTA', 'VOLKSWAGEN', 'SKODA', 'KIA', 'NISSAN'])
#     df2 = pd.DataFrame(data2, columns=['Mėnuo', 'VOLKSWAGEN', 'BMW', 'AUDI', 'TOYOTA', 'OPEL'])
#     print(df1)
#     print(df2)
#     df1.to_csv('populiariausios_naujos_markes_2022.csv')
#     df2.to_csv('populiariausios_senos_markes_2022.csv')

# 2021 METU DUOMENYS:
# NAUJU IR NAUDOTU AUTOMOBILIU POPULIARUMAS:

# url = 'https://www.regitra.lt/lt/atviri-duomenys/?datayear=2021&dataquery='
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# tables = soup.find_all('table', class_='grey large left')
# if len(tables) >= 2:
#     data1 = []
#     data2 = []
#     # Pirmoji lentelė
#     rows = tables[1].find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         if len(columns) >= 6:
#             data1.append({
#                 'Mėnuo': columns[0].text.strip(),
#                 'FIAT': columns[1].text.strip(),
#                 'TOYOTA': columns[2].text.strip(),
#                 'VOLKSWAGEN': columns[3].text.strip(),
#                 'SKODA': columns[4].text.strip(),
#                 'PEUGEOT': columns[5].text.strip(),
#
#             })
#     # Antroji lentelė
#     rows = tables[2].find_all('tr')
#     for row in rows[1:]:
#         columns = row.find_all('td')
#         if len(columns) >= 6:
#             data2.append({
#                 'Mėnuo': columns[0].text.strip(),
#                 'VOLKSWAGEN': columns[1].text.strip(),
#                 'BMW': columns[2].text.strip(),
#                 'AUDI': columns[3].text.strip(),
#                 'TOYOTA': columns[5].text.strip(),
#                 'OPEL': columns[4].text.strip()
#             })
#     df1 = pd.DataFrame(data1, columns=['Mėnuo', 'FIAT', 'TOYOTA', 'VOLKSWAGEN', 'SKODA', 'PEUGEOT'])
#     df2 = pd.DataFrame(data2, columns=['Mėnuo', 'VOLKSWAGEN', 'BMW', 'AUDI', 'OPEL', 'TOYOTA'])
#     print(df1)
#     print(df2)
#     df1.to_csv('populiariausios_naujos_markes_2021.csv')
#     df2.to_csv('populiariausios_senos_markes_2021.csv')
#

# DUOMENU TVARTKYMAS TOLESNEI ANALIZEI:

# prie nauju populiauriusiu markiu 2021 pridejome stulpeli
# su visais pirkimais pamenesiui is automobiliu registracijos 2021


# populiariausios_naujos_markes_2021_new = pd.read_csv('Files_csv/populiariausios_naujos_markes_2021.csv')
# automobiliu_registracija_2021 = pd.read_csv('Files_csv/automobiliu_registracija_2021.csv')
# nauji_automobiliai_M1 = automobiliu_registracija_2021['Is ju M1 klases nauju lengvuju automobiliu']
# populiariausios_naujos_markes_2021_new['Is ju M1 klases nauju lengvuju automobiliu'] = nauji_automobiliai_M1
# populiariausios_naujos_markes_2021_new.to_csv('Files_csv/populiariausios_naujos_markes_2021_new.csv', index=False)

# prie nauju populiauriusiu markiu 2022 pridejome stulpeli
# su visais pirkimais pamenesiui is automobiliu registracijos 2021


# populiariausios_naujos_markes_2022_new = pd.read_csv('Files_csv/populiariausios_naujos_markes_2022.csv')
# automobiliu_registracija_2022 = pd.read_csv('Files_csv/automobiliu_registracija_2022.csv')
# nauji_automobiliai_M1_2022 = automobiliu_registracija_2022['Is ju M1 klases nauju lengvuju automobiliu']
# populiariausios_naujos_markes_2022_new['Is ju M1 klases nauju lengvuju automobiliu'] = nauji_automobiliai_M1_2022
# populiariausios_naujos_markes_2022_new.to_csv('Files_csv/populiariausios_naujos_markes_2022_new.csv', index=False)

# POPULIARIAUSIU MARKIU ANALIZE:

#TIKSLAS: nustatyti procentine populiariausiu M1 klases nauju automobiliu dali nuo
# visu naujai registruotu transporto priemoniu 2021:

# df = pd.read_csv('Files_csv/populiariausios_naujos_markes_2021_new.csv', skipfooter=1, engine='python')
# df = df[df['Unnamed: 0'] != 'Iš viso']
# df['FIAT'] = df['FIAT'].astype(int)
# df['TOYOTA'] = df['TOYOTA'].astype(int)
# df['VOLKSWAGEN'] = df['VOLKSWAGEN'].astype(int)
# df['SKODA'] = df['SKODA'].astype(int)
# df['PEUGEOT'] = df['PEUGEOT'].astype(int)
# df['FIAT_procentai'] = (df['FIAT'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
# df['TOYOTA_procentai'] = (df['TOYOTA'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
# df['VOLKSWAGEN_procentai'] = (df['VOLKSWAGEN'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
# df['SKODA_procentai'] = (df['SKODA'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
# df['PEUGEOT_procentai'] = (df['PEUGEOT'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
# plt.figure(figsize=(10, 6))
# plt.plot(df['Mėnuo'], df['FIAT_procentai'], label='FIAT', marker='o')
# plt.plot(df['Mėnuo'], df['TOYOTA_procentai'], label='TOYOTA', marker='o')
# plt.plot(df['Mėnuo'], df['VOLKSWAGEN_procentai'], label='VOLKSWAGEN', marker='o')
# plt.plot(df['Mėnuo'], df['SKODA_procentai'], label='SKODA', marker='o')
# plt.plot(df['Mėnuo'], df['PEUGEOT_procentai'], label='PEUGEOT', marker='o')
# plt.xlabel('Mėnuo')
# plt.ylabel('Procentai nuo visų naujų M1 automobilių')
# plt.title('Procentinė populiariausiu M1 klases nauju automobiliu dalis nuo visu nauju registruotu 2021 m.')
# plt.xticks(rotation=45)
# plt.legend()
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.tight_layout()
# plt.show()


# Procentinė populiariausiu M1 klases nauju automobiliu dalis nuo visu nauju registruotu 2022

df = pd.read_csv('Files_csv/populiariausios_naujos_markes_2022_new.csv',skipfooter=1, engine='python')
df = df[df['Unnamed: 0'] != 'Iš viso']

# # 2022 m populiariausiu automobiliu markes skiriasi
#
# df['TOYOTA'] = df['TOYOTA'].astype(int)
# df['VOLKSWAGEN'] = df['VOLKSWAGEN'].astype(int)
# df['SKODA'] = df['SKODA'].astype(int)
# df['KIA'] = df['KIA'].astype(int)
# df['NISSAN'] = df['NISSAN'].astype(int)
# df['TOYOTA_procentai'] = (df['TOYOTA'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
# df['VOLKSWAGEN_procentai'] = (df['VOLKSWAGEN'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
# df['SKODA_procentai'] = (df['SKODA'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
# df['KIA_procentai'] = (df['KIA'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
# df['NISSAN_procentai'] = (df['NISSAN'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
# plt.figure(figsize=(10, 6))
#
# plt.plot(df['Mėnuo'], df['TOYOTA_procentai'], label='TOYOTA', marker='o')
# plt.plot(df['Mėnuo'], df['VOLKSWAGEN_procentai'], label='VOLKSWAGEN', marker='o')
# plt.plot(df['Mėnuo'], df['SKODA_procentai'], label='SKODA', marker='o')
# plt.plot(df['Mėnuo'], df['KIA_procentai'], label='KIA', marker='o')
# plt.plot(df['Mėnuo'], df['NISSAN_procentai'], label='NISSAN', marker='o')
# plt.xlabel('Mėnuo')
# plt.ylabel('Procentai nuo visų naujų M1 automobilių')
# plt.title('Procentinė populiariausiu M1 klases nauju automobiliu dalis nuo visu nauju registruotu 2022 m.')
# plt.xticks(rotation=45)
# plt.legend()
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.tight_layout()
# plt.show()

# ISVADA: 2021/2022 LYGINAMOJI ANALIZE PARODO, KAD VYRAUJA TOS PACIOS MARKES, TACIAU
# 2022 M. TOYOTA POPULIARUMAS ISAUGO DEL IMONES VYKDOMOS INTENSYVIOS AKCIJU POLITIKOS IR DEL
# ISPLESTOS HIBRIDINIU TRANSPORTO PRIEMONIU PASIULOS IR PALANKIU FINANSAVIMO SALYGU.


# TIKSLAS: ATLIKTI NAUJU IVEZAMU TRANSPORTO PRIEMONIU PROGNOZE ATEINANTIEMS 5 METAMS
#
# data = {
#     'Metai': [2018, 2019, 2020, 2021, 2022],
#     'Automobiliu_sk': [60179, 72589, 59560, 61475, 56498]
# }
# df = pd.DataFrame(data)
# # Paruošiame duomenis modeliui
# X = df['Metai'].values.reshape(-1,1)
# y = df['Automobiliu_sk'].values
# # Apmokome modelį
# model = LinearRegression().fit(X, y)
# # Gaukime prognozę ateinantiems 5 metams
# ateinanciu_metu_skaicius = 5
# ateinanciu_metu_prognoze = np.array(range(2023, 2023 + ateinanciu_metu_skaicius)).reshape(-1, 1)
# predicted_values = model.predict(ateinanciu_metu_prognoze)
# # Pavaizduokime istorinius duomenis ir prognozę grafike
# plt.figure(figsize=(10, 6))
# plt.scatter(df['Metai'], df['Automobiliu_sk'], color='blue', label='Istoriniai duomenys')
# plt.plot(ateinanciu_metu_prognoze, predicted_values, color='red', linestyle='-', marker='o', label='Prognozė')
# plt.xlabel('Metai')
# plt.ylabel('Automobilių skaičius')
# plt.title('Naujų automobilių įvežimo prognozė')
# plt.legend()
# plt.grid(True)
# plt.show()

# ISVADA: NAUDOJANT TIESINES REGRESIJOS PROGNOZAVIMO METODA, MATYTI, KAD ISLIEKA
# NAUJU TRANSPORTO PRIEMONIU IVEZIMO MAZEJIMO TENDENCIJA. ISTORISKAI RODIKLIAMS ITAKOS
# TUREJO: PANDEMIJA, PUSLAIDININKIU DEFICITAS, UKRAINOS KARAS, EURIBOR KILIMAS
# IR INFLIACIJA