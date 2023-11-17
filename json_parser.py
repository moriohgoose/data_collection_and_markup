import requests
import json
import pandas as pd
import time

cookies = {
    '_ga': 'GA1.2.1197745738.1700003762',
    '_gid': 'GA1.2.1216452692.1700003762',
    '_gat_UA-109101508-1': '1',
    '_ga_5N56DS01PN': 'GS1.2.1700043936.2.1.1700044075.0.0.0',
}

headers = {
    'authority': 'thegameawards.com',
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    # 'cookie': '_ga=GA1.2.1197745738.1700003762; _gid=GA1.2.1216452692.1700003762; _gat_UA-109101508-1=1; _ga_5N56DS01PN=GS1.2.1700043936.2.1.1700044075.0.0.0',
    'referer': 'https://thegameawards.com/nominees',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.837 YaBrowser/23.9.4.837 Yowser/2.5 Safari/537.36',
    'x-nextjs-data': '1',
}

start_time = time.time()

response = requests.get(
    'https://thegameawards.com/_next/data/qr8Ssd2cLTqzcGOhCbMnr/nominees.json',
    cookies=cookies,
    headers=headers,
    timeout=(60,60),
)

end_time = time.time()
print(f"Request took {end_time - start_time} seconds")

if response.ok:
    analyze_data = json.loads(response.text)
    df = pd.DataFrame(columns=['award_name','game_name','studio'])
    awards = analyze_data['pageProps']['awards']


    for award in awards:
        award_name = award['name']
        
        for nominee in award['nominees']:
            game_name = nominee['name']
            studio = nominee['caption']
            
            df = df._append({'award_name': award_name, 'game_name': game_name, 'studio': studio}, ignore_index=True)

    df.to_csv('the_game_awards_2023.csv', index=False)
