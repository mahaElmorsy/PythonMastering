import requests

API_KEY = 'fca_live_zDL3B0Q9IUzO1SYdDluBGPXnjhn69fT2djuZZ81c'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ['EUR', 'USD', 'CAD', 'AUD']


def convert_currency(base):
    currencies = ','.join(CURRENCIES)
    search_url = f'{BASE_URL}&base_currency={base}&currencies={currencies}'

    try:
        response = requests.get(search_url)
        data = response.json()
        return data['data']
    except:
        print('Sorry but the currency you entered is Invalid currency or not included in this API')
        return None


while True:

    base = input('Enter the base currency (and q for quit) : ').upper()
    if base == 'Q':
        break
    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for curr, value in data.items():
        print(f'{base} to {curr} = {value}')
