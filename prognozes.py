
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

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

# TIKSLAS: ATLIKTI KLIMATO KAITAI TVARESNIU IVEZAMU TRANSPORTO PRIEMONIU PROGNOZE ATEINANTIEMS 5 METAMS

# TIK ELEKTRA VAROMI:
# data = {
#     'Metai': [2018, 2019, 2020, 2021, 2022],
#     'Automobiliu_sk': [969, 1397, 2496, 4841, 7346]
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
# plt.title('Elektromobiliu įvežimo prognozė')
# plt.legend()
# plt.grid(True)
# plt.show()


#  HIBRIDAI(BENZINAS/ELEKTRA):
#
# data = {
#     'Metai': [2018, 2019, 2020, 2021, 2022],
#     'Automobiliu_sk': [13378, 19594, 26894, 36536, 49151]
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
# plt.title('Hibridu įvežimo prognozė')
# plt.legend()
# plt.grid(True)
# plt.show()

# ISVADA: NAUDOJANT TIESINES REGRESIJOS PROGNOZAVIMO METODA, MATYTI, KAD LIETUVOJE IR TOLIAU ISLIKS
# ELEKTRINIU IR HIBRIDINIU TRANSPORTO PRIEMONIU AUGIMO TENDENCIJA
