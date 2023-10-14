from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np



# # is viso registracijos lentele 2021- 2022
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
# # df.to_csv('automobiliu_registracija_2021.csv')
#
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
#
# # df.to_csv('automobiliu_registracija_2022.csv')
#
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
# plt.savefig('Grafikai/Transporto_registracija_2021.jpg')
# plt.show()
#
#
# df = pd.read_csv('Files_csv/automobiliu_registracija_2022.csv', skipfooter=1, engine='python')
# df['Is viso registruota'] = df['Is viso naudotu transporto priemoniu']+df['Is viso nauju transporto priemoniu']
# naujas_df_2022 = df[['Menuo', 'Is viso registruota']].copy()
# print(naujas_df_2022)
# plt.figure(figsize=(10,6))
# plt.bar(naujas_df_2022['Menuo'], naujas_df_2022['Is viso registruota'])
# plt.xlabel('Menuo')
# plt.ylabel('Is viso registruota')
# plt.title('Transporto_registracija_2022')
# plt.xticks(rotation=45)
# plt.savefig('Grafikai/Transporto_registracija_2022.jpg')
# plt.show()

