from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# TIKSLAS: NUSTATYTI, KOKIOS TRANSPORTO PRIEMONIU MARKES YRA POPULIARIAUSIOS LIETUVOJE.

# NAUJU IR NAUDOTU AUTOMOBILIU POPULIARUMO LENTELES:
#
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
# #     df1.to_csv('populiariausios_naujos_markes_2022.csv')
# #     df2.to_csv('populiariausios_senos_markes_2022.csv')
#
# # 2021 METU DUOMENYS:
# # NAUJU IR NAUDOTU AUTOMOBILIU POPULIARUMAS:
#
# url = 'https://www.regitra.lt/lt/atviri-duomenys/?datayear=2021&dataquery='
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# tables = soup.find_all('table', class_='grey large left')
# if len(tables) >= 2:
#     data1 = []
#     data2 = []
# #     # Pirmoji lentelė
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
# #     # Antroji lentelė
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

# prie nauju populiariausiu markiu 2021 pridejome stulpeli
# su visais pirkimais pamenesiui is automobiliu registracijos 2021


# populiariausios_naujos_markes_2021_new = pd.read_csv('Files_csv/populiariausios_naujos_markes_2021.csv')
# automobiliu_registracija_2021 = pd.read_csv('Files_csv/automobiliu_registracija_2021.csv')
# nauji_automobiliai_M1 = automobiliu_registracija_2021['Is ju M1 klases nauju lengvuju automobiliu']
# populiariausios_naujos_markes_2021_new['Is ju M1 klases nauju lengvuju automobiliu'] = nauji_automobiliai_M1
# populiariausios_naujos_markes_2021_new.to_csv('Files_csv/populiariausios_naujos_markes_2021_new.csv', index=False)
#
# # prie nauju populiauriusiu markiu 2022 pridejome stulpeli
# # su visais pirkimais pamenesiui is automobiliu registracijos 2022
#
#
# populiariausios_naujos_markes_2022_new = pd.read_csv('Files_csv/populiariausios_naujos_markes_2022.csv')
# automobiliu_registracija_2022 = pd.read_csv('Files_csv/automobiliu_registracija_2022.csv')
# nauji_automobiliai_M1_2022 = automobiliu_registracija_2022['Is ju M1 klases nauju lengvuju automobiliu']
# populiariausios_naujos_markes_2022_new['Is ju M1 klases nauju lengvuju automobiliu'] = nauji_automobiliai_M1_2022
# populiariausios_naujos_markes_2022_new.to_csv('Files_csv/populiariausios_naujos_markes_2022_new.csv', index=False)

# POPULIARIAUSIU NAUJU MARKIU ANALIZE:

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
# plt.title('Procentinė populiariausių M1 klasės naujų automobilių dalis nuo visu naujų registruotų 2021 m.')
# plt.xticks(rotation=45)
# plt.legend()
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.tight_layout()
# plt.savefig('Grafikai/Procentine_pop_M1_nauju_auto_dalis_nuo_visu_nauju_registruotu_2021.jpg')
# plt.show()

#
# # Procentinė populiariausiu M1 klases nauju automobiliu dalis nuo visu nauju registruotu 2022
#
df = pd.read_csv('Files_csv/populiariausios_naujos_markes_2022_new.csv',skipfooter=1, engine='python')
df = df[df['Unnamed: 0'] != 'Iš viso']
#
# # # 2022 m populiariausiu automobiliu markes skiriasi
# #
df['TOYOTA'] = df['TOYOTA'].astype(int)
df['VOLKSWAGEN'] = df['VOLKSWAGEN'].astype(int)
df['SKODA'] = df['SKODA'].astype(int)
df['KIA'] = df['KIA'].astype(int)
df['NISSAN'] = df['NISSAN'].astype(int)
df['TOYOTA_procentai'] = (df['TOYOTA'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
df['VOLKSWAGEN_procentai'] = (df['VOLKSWAGEN'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
df['SKODA_procentai'] = (df['SKODA'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
df['KIA_procentai'] = (df['KIA'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
df['NISSAN_procentai'] = (df['NISSAN'] / df['Is ju M1 klases nauju lengvuju automobiliu']) * 100
plt.figure(figsize=(10, 6))
#
plt.plot(df['Mėnuo'], df['TOYOTA_procentai'], label='TOYOTA', marker='o')
plt.plot(df['Mėnuo'], df['VOLKSWAGEN_procentai'], label='VOLKSWAGEN', marker='o')
plt.plot(df['Mėnuo'], df['SKODA_procentai'], label='SKODA', marker='o')
plt.plot(df['Mėnuo'], df['KIA_procentai'], label='KIA', marker='o')
plt.plot(df['Mėnuo'], df['NISSAN_procentai'], label='NISSAN', marker='o')
plt.xlabel('Mėnuo')
plt.ylabel('Procentai nuo visų naujų M1 automobilių')
plt.title('Procentinė populiariausių M1 klasės naujų automobilių dalis nuo visų naujų registruotų 2022 m.')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig('Grafikai/Procentine_pop_M1_nauju_auto_dalis_nuo_visu_nauju_registruotu_2022.jpg')
plt.show()

# ISVADA: 2021/2022 LYGINAMOJI ANALIZE PARODO, KAD VYRAUJA TOS PACIOS MARKES, TACIAU
# 2022 M. TOYOTA POPULIARUMAS ISAUGO DEL IMONES VYKDOMOS INTENSYVIOS AKCIJU POLITIKOS IR DEL
# ISPLESTOS HIBRIDINIU TRANSPORTO PRIEMONIU PASIULOS IR PALANKIU FINANSAVIMO SALYGU.

# POPULIARIAUSIOS NAUDOTU M1 KLASES AUTOMOBILIU MARKES:
# prie naudotu populiariausiu markiu 2021 pridejome stulpeli
# su visais pirkimais pamenesiui is automobiliu registracijos 2021


# populiariausios_naudotos_markes_2021_new = pd.read_csv('Files_csv/populiariausios_senos_markes_2021.csv')
# automobiliu_registracija_2021 = pd.read_csv('Files_csv/automobiliu_registracija_2021.csv')
# naudoti_automobiliai_M1 = automobiliu_registracija_2021['Is ju M1 klases naudotu lengvuju automobiliu']
# populiariausios_naudotos_markes_2021_new['Is ju M1 klases naudotu lengvuju automobiliu'] = naudoti_automobiliai_M1
# populiariausios_naudotos_markes_2021_new.to_csv('Files_csv/populiariausios_naudotos_markes_2021_new.csv', index=False)

# prie naudotu populiauriusiu markiu 2022 pridejome stulpeli
# su visais pirkimais pamenesiui is automobiliu registracijos 2022


# populiariausios_naudotos_markes_2022_new = pd.read_csv('Files_csv/populiariausios_senos_markes_2022.csv')
# automobiliu_registracija_2022 = pd.read_csv('Files_csv/automobiliu_registracija_2022.csv')
# naudoti_automobiliai_M1_2022 = automobiliu_registracija_2022['Is ju M1 klases naudotu lengvuju automobiliu']
# populiariausios_naudotos_markes_2022_new['Is ju M1 klases naudotu lengvuju automobiliu'] = naudoti_automobiliai_M1_2022
# populiariausios_naudotos_markes_2022_new.to_csv('Files_csv/populiariausios_naudotos_markes_2022_new.csv', index=False)

# POPULIARIAUSIU NAUDOTU MARKIU ANALIZE:

# TIKSLAS: nustatyti procentine populiariausiu M1 klases naudotu automobiliu dali nuo
# visu naujai registruotu transporto priemoniu 2021:

# df = pd.read_csv('Files_csv/populiariausios_naudotos_markes_2021_new.csv', skipfooter=1, engine='python')
# df = df[df['Unnamed: 0'] != 'Iš viso']
# df['VOLKSWAGEN'] = df['VOLKSWAGEN'].astype(int)
# df['BMW'] = df['BMW'].astype(int)
# df['AUDI'] = df['AUDI'].astype(int)
# df['OPEL'] = df['OPEL'].astype(int)
# df['TOYOTA'] = df['TOYOTA'].astype(int)
# df['VOLKSWAGEN_procentai'] = (df['VOLKSWAGEN'] / df['Is ju M1 klases naudotu lengvuju automobiliu']) * 100
# df['BMW_procentai'] = (df['BMW'] / df['Is ju M1 klases naudotu lengvuju automobiliu']) * 100
# df['AUDI_procentai'] = (df['AUDI'] / df['Is ju M1 klases naudotu lengvuju automobiliu']) * 100
# df['OPEL_procentai'] = (df['OPEL'] / df['Is ju M1 klases naudotu lengvuju automobiliu']) * 100
# df['TOYOTA_procentai'] = (df['TOYOTA'] / df['Is ju M1 klases naudotu lengvuju automobiliu']) * 100
# plt.figure(figsize=(10, 6))
# plt.plot(df['Mėnuo'], df['VOLKSWAGEN_procentai'], label='VOLKSWAGEN', marker='o')
# plt.plot(df['Mėnuo'], df['BMW_procentai'], label='BMW', marker='o')
# plt.plot(df['Mėnuo'], df['AUDI_procentai'], label='AUDI', marker='o')
# plt.plot(df['Mėnuo'], df['OPEL_procentai'], label='OPEL', marker='o')
# plt.plot(df['Mėnuo'], df['TOYOTA_procentai'], label='TOYOTA', marker='o')
# plt.xlabel('Mėnuo')
# plt.ylabel('Procentai nuo visų naudotų M1 automobilių')
# plt.title('Procentinė populiariausių M1 klases naudotų automobilių dalis nuo visų registruotų 2021 m.')
# plt.xticks(rotation=45)
# plt.legend()
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.tight_layout()
# plt.savefig('Grafikai/Procentine_pop_M1_naudotu_auto_dalis_nuo_visu_naudotu_registruotu_2021.jpg')
# plt.show()


# Procentinė populiariausiu M1 klases naudotu automobiliu dalis nuo visu naudotu registruotu 2022

# df = pd.read_csv('Files_csv/populiariausios_naudotos_markes_2022_new.csv',skipfooter=1, engine='python')
# df = df[df['Unnamed: 0'] != 'Iš viso']

# # 2022 m populiariausiu naudotu automobiliu markes skiriasi

# df['VOLKSWAGEN'] = df['VOLKSWAGEN'].astype(int)
# df['BMW'] = df['BMW'].astype(int)
# df['AUDI'] = df['AUDI'].astype(int)
# df['TOYOTA'] = df['TOYOTA'].astype(int)
# df['OPEL'] = df['OPEL'].astype(int)
#
# df['VOLKSWAGEN_procentai'] = (df['VOLKSWAGEN'] / df['Is ju M1 klases naudotu lengvuju automobiliu']) * 100
# df['BMW_procentai'] = (df['BMW'] / df['Is ju M1 klases naudotu lengvuju automobiliu']) * 100
# df['AUDI_procentai'] = (df['AUDI'] / df['Is ju M1 klases naudotu lengvuju automobiliu']) * 100
# df['TOYOTA_procentai'] = (df['TOYOTA'] / df['Is ju M1 klases naudotu lengvuju automobiliu']) * 100
# df['OPEL_procentai'] = (df['OPEL'] / df['Is ju M1 klases naudotu lengvuju automobiliu']) * 100
#
# plt.figure(figsize=(10, 6))
# plt.plot(df['Mėnuo'], df['VOLKSWAGEN_procentai'], label='VOLKSWAGEN', marker='o')
# plt.plot(df['Mėnuo'], df['BMW_procentai'], label='BMW', marker='o')
# plt.plot(df['Mėnuo'], df['AUDI_procentai'], label='AUDI', marker='o')
# plt.plot(df['Mėnuo'], df['TOYOTA_procentai'], label='TOYOTA', marker='o')
# plt.plot(df['Mėnuo'], df['OPEL_procentai'], label='OPEL', marker='o')
#
# plt.xlabel('Mėnuo')
# plt.ylabel('Procentai nuo visų naudotų M1 automobilių')
# plt.title('Procentinė populiariausių M1 klasės naudotų automobilių dalis nuo visų registruotų 2022 m.')
# plt.xticks(rotation=45)
# plt.legend()
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.tight_layout()
# plt.savefig('Grafikai/Procentine_pop_M1_naudotu_auto_dalis_nuo_visu_naudotu_registruotu_2022.jpg')
# plt.show()
#
# ISVADA: NAUDOTŲ M1 KL. AUTOMOBILIŲ SEGMENTE DOMINUOJA VOKIŠKOS MARKĖS SU TARŠESNIAIS
# GAMTAI VIDAUS DEGIMO VARIKLIAIS.
