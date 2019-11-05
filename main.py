import requests
import credentials
from time import sleep
import telegram

bot = telegram.Bot(token=credentials.TOKEN)


def telegram_send_message(bot_message):
    send_text = 'https://api.telegram.org/bot' + credentials.TOKEN + '/sendMessage?chat_id=' + credentials.GROUP_CHAT_ID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

params = {
  'city': 'Almaty'
}

api_result = requests.get('http://api.weatherstack.com/current?access_key=9a2c47630fa21a89a1cd9653c32f7838&query=' + params['city'])

api_response = api_result.json()

# print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))
# bot.send_message(chat_id=credentials.GROUP_CHAT_ID, text="HELLO")

updates = bot.get_updates()

for update in updates:
    if update.message:
        print(update.message.text)

#print([u.message for u in updates])