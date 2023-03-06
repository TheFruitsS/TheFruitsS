

import pandas as pd
import requests


def scrape(urls):

    res = requests.get(urls)

    if res.status_code == 200:
        df = pd.read_json('https://jsonplaceholder.typicode.com/users')
        data = df.to_dict()
        data_names = dict(data['name'])

        data_adress = dict(data['address'])
        #fill the database with namess
        # names = [x for x in data_names.values()]
        # names_lists = []
        # for x in names:
        #     names_lists.append([x])
        print(data_adress.values())

        return





url = 'https://jsonplaceholder.typicode.com/users'


data = scrape(url)

