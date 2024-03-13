import requests, pandas_gbq, pandas

baseurl = 'https://rickandmortyapi.com/api/'
end_point = 'character'

def main_request(base_url, endpoint, page_no):
    response = requests.get(base_url+endpoint+f'?page={page_no}')
    return response.json()

def get_pages(response):
    return response['info']['pages']

def character_episodes(response):
    chars_list = []
    for item in response['results']:
        char = {
                'Name': item['name'],
                'Location': item['location']['name'], 
                'Episodes': len(item['episode'])
                }
        chars_list.append(char)
    return chars_list

data = main_request(baseurl, end_point, 3)

all_chars_list = []

for page in range(1, get_pages(data)+1):
    all_chars_list.extend(character_episodes(main_request(baseurl, end_point, page)))

print(all_chars_list)

chars_df = pandas.DataFrame(all_chars_list)
print(chars_df.head())
pandas_gbq.to_gbq(chars_df, 'ferrous-record-386911.api.chars', project_id='ferrous-record-386911', if_exists='append')