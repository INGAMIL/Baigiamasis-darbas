from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt


# is viso registracijos lentele 2021- 2022-2023
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

# df = pd.read_csv('automobiliu_registracija_2021.csv', skipfooter=1, engine='python')
# df['Is viso registruota'] = df['Is viso naudotu transporto priemoniu']+df['Is viso nauju transporto priemoniu']
# naujas_df_2021 = df[['Menuo', 'Is viso registruota']].copy()
#
# print(naujas_df_2021)
# plt.figure(figsize=(10,6))
# plt.bar(naujas_df_2021['Menuo'], naujas_df_2021['Is viso registruota'])
# plt.xlabel('Menuo')
# plt.ylabel('Is viso registruota')
# plt.title('Transporto registracija 2021')
# plt.xticks(rotation=45)
# plt.show()

# df = pd.read_csv('automobiliu_registracija_2022.csv', skipfooter=1, engine='python')
# df['Is viso registruota'] = df['Is viso naudotu transporto priemoniu']+df['Is viso nauju transporto priemoniu']
# naujas_df_2022 = df[['Menuo', 'Is viso registruota']].copy()
# print(naujas_df_2022)
# plt.figure(figsize=(10,6))
# plt.bar(naujas_df_2022['Menuo'], naujas_df_2022['Is viso registruota'])
# plt.xlabel('Menuo')
# plt.ylabel('Is viso registruota')
# plt.title('Transporto registracija 2022')
# plt.xticks(rotation=45)
# plt.show()

# data_files = [('automobiliu_registracija_2021.csv', '2021'),
#               ('automobiliu_registracija_2022.csv', '2022')]
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

# data_files = [('automobiliu_registracija_2021.csv', '2021'),
#               ('automobiliu_registracija_2022.csv', '2022')]
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

# data_files = [('automobiliu_registracija_2021.csv', '2021'),
#               ('automobiliu_registracija_2022.csv', '2022')]
# plt.figure(figsize=(12, 8))
# bar_width = 0.35  # stulpelio plotis
# index = range(len(pd.read_csv(data_files[0][0], skipfooter=1, engine='python')['Menuo']))  # stulpelių indeksai
# for i, (data_file, year) in enumerate(data_files):
#     df = pd.read_csv(data_file, skipfooter=1, engine='python')
#     # Sukurti stulpelius naudotoms transporto priemonėms
#     plt.bar([ind + bar_width * i for ind in index], df['Is viso naudotu transporto priemoniu'], width=bar_width, label=f'Naudoti {year}', alpha=0.7)
#     # Sukurti stulpelius naujoms transporto priemonėms
#     plt.bar([ind + bar_width * i for ind in index], df['Is viso nauju transporto priemoniu'], width=bar_width, bottom=df['Is viso naudotu transporto priemoniu'], label=f'Nauji {year}', alpha=0.7)
# plt.xlabel('Menuo')
# plt.ylabel('Is viso registruota')
# plt.title('Transporto registracija 2021 vs 2022')
# plt.xticks([ind + bar_width / 2 for ind in index], df['Menuo'], rotation=45)
# plt.legend()
# plt.tight_layout()
# plt.show()

# naujų automobilių procentinė dalis nuo viso registruotų automobilių kiekvienais metais.

# data_files = [('automobiliu_registracija_2021.csv', '2021'),
#               ('automobiliu_registracija_2022.csv', '2022')]
# procentai = []
# for data_file, year in data_files:
#     df = pd.read_csv(data_file, skipfooter=1, engine='python')
#     nauji = df['Is viso nauju transporto priemoniu'].sum()
#     viso = df['Is viso naudotu transporto priemoniu'].sum() + nauji
#     procentine_dalis = (nauji / viso) * 100
#     procentai.append(procentine_dalis)
# # Nubraizome grafiką
# plt.bar([year for _, year in data_files], procentai, color=['blue', 'green'])
# plt.xlabel('Metai')
# plt.ylabel('Procentai')
# plt.title('Naujų automobilių procentinė dalis nuo viso registruotų automobilių')
# plt.ylim(0, 100)  # Nustatome Y ašies ribas nuo 0 iki 100
# plt.show()

# data_files = [('automobiliu_registracija_2021.csv', '2021'),
#               ('automobiliu_registracija_2022.csv', '2022')]
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



# df['Is viso registruota'] = df['Is viso naudotu transporto priemoniu']+df['Is viso nauju transporto priemoniu']
# naujas_df = df[['Menuo', 'Is viso registruota']].copy()
# plt.figure(figsize=(10,6))
# plt.bar(naujas_df['Menuo'], naujas_df['Is viso registruota'])
# plt.xlabel('Menuo')
# plt.ylabel('Is viso registruota')
# plt.title('Transporto registracija 2022')
# plt.xticks(rotation=45)
# plt.show()

# url = 'https://www.regitra.lt/lt/atviri-duomenys/?datayear=2023&dataquery='
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
# df.to_csv('automobiliu_registracija_2023.csv')

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

# ANALIZE NAUJU AUTOMOBILIU POPULIARUMO 2021 VS 2022:
# nebaigta!!!!!
# data_file = [('populiariausios_naujos_markes_2021.csv', '2021')
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