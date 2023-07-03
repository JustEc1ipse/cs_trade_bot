import requests
from bs4 import BeautifulSoup
import json

url = 'https://steamcommunity.com/market/search?appid=730'

response = requests.get(url)
soup = BeautifulSoup(response.text , 'html.parser')

item_blocks = soup.find_all('a' , class_ = 'market_listing_row_link')

items = []
item_blocks = item_blocks[:10]
for item_block in item_blocks:
    item_name = item_block.find('span',
class_='market_listing_item_name').text.strip()
    item_price = item_block.find('span',
class_='normal_price').text.strip()

item_info = {'item_name': item_name , 'item_price':item_price}
items.append(item_info)

bot_token = '6345303348:AAHJYdv3YRhEorcFB05Z07uoigiXWhJM4bo'
chat_id = '6345303348'

message = 'Info about items:\n'
for item in items:
    message += f"Name: {item['name']}, Price: {item['price']}\n"

telegram_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
data = {'chat_id': chat_id, 'text': message}

response = requests.post(telegram_url, data=data)