import json
from operator import itemgetter

with open('../Dados_das_Raspagens/bistek.json') as bistek:
    bistek_data = json.load(bistek)

    for i, j in enumerate(bistek_data):
        bistek_data[i]['price'] = float(bistek_data[i]['price'].replace(',', '.'))

    sorted_price1 = sorted(bistek_data, key=itemgetter('price'), reverse=False)

    for i in sorted_price1:
        print(i)


with open('../Dados_das_Raspagens/angeloni.json') as angeloni:
    angeloni_data = json.load(angeloni)

    for i, j in enumerate(angeloni_data):
        angeloni_data[i]['price'] = angeloni_data[i]['price'].replace('.', '')
        angeloni_data[i]['price'] = float(angeloni_data[i]['price'].replace(',', '.'))

    sorted_price2 = sorted(angeloni_data, key=itemgetter('price'), reverse=False)

    print(3*'\n')
    print('{}NOW WE ARE GOING TO SEE ANGELONI PRODUCTS{}'.format('\033[4;34m', '\033[m'))
    print(3*'\n')

    for i in sorted_price2:
        print(i)
#
