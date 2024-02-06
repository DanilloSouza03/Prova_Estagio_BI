import requests
import pandas as pd
import time

capitais_brasil = {
    'AC': 'Rio Branco',
    'AL': 'Maceio',
    'AP': 'Macapa',
    'AM': 'Manaus',
    'BA': 'Salvador',
    'CE': 'Fortaleza',
    'DF': 'Brasilia',
    'ES': 'Vitoria',
    'GO': 'Goiania',
    'MA': 'Sao Luis',
    'MT': 'Cuiaba',
    'MS': 'Campo Grande',
    'MG': 'Belo Horizonte',
    'PA': 'Belem',
    'PB': 'Joao Pessoa',
    'PR': 'Curitiba',
    'PE': 'Recife',
    'PI': 'Teresina',
    'RJ': 'Rio de Janeiro',
    'RN': 'Natal',
    'RS': 'Porto Alegre',
    'RO': 'Porto Velho',
    'RR': 'Boa Vista',
    'SC': 'Florianopolis',
    'SP': 'Sao Paulo',
    'SE': 'Aracaju',
    'TO': 'Palmas'
}

dados_ceps = []

for uf, cidade in capitais_brasil.items():
    url = f'https://viacep.com.br/ws/{uf}/{cidade}/Praça/json/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        dados_ceps.extend(data)
    else:
        print(f'Erro na Cidade:{cidade}')

    time.sleep(5)


df = pd.DataFrame(dados_ceps)
df.to_csv('dados_cep.csv', encoding='utf-8', sep=';', index=False)
print('Dados salvos em dados_cep.csv.')