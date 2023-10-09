from bs4 import BeautifulSoup
import requests
import pandas as pd

# url = 'https://www.regitra.lt/lt/atviri-duomenys/'
# response = requests.get(url)
# print(response.status_code)

# url ='https://www.autotyrimai.lt/barometras/'
# response = requests.get(url)
# print(response.status_code)

# df = pd.read_excel('transporto-priemoniu-parko-vidutinis-amzius-pagal-kategorijas-2023-m-sausio-1-d-duomenys.xlsx')
# df = pd.read_excel('4-transporto-priemoniu-parko-duomenys-pagal-degalu-rusi-2023-m-rugpjucio-1-d-duomenys.xlsx')
# df = pd.read_excel('6-iregistruotu-transporto-priemoniu-skaicius-pagal-degalu-rusi-ir-savivaldybes-2023-m-rugpjucio-1-d-duomenys.xlsx')
df = pd.read_excel('3-lietuvos-respublikos-keliu-transporto-priemoniu-registre-pirma-karta-iregistruotu-m1-klases-transporto-priemoniu-skaicius-pagal-eksporto-sali.xlsx')
print(df)