import requests
import credentials
from time import sleep
import telegram

bot = telegram.Bot(token=credentials.TOKEN)


def telegram_send_message(bot_message):
    send_text = 'https://api.telegram.org/bot' + \
                credentials.TOKEN + '/sendMessage?chat_id=' + \
                credentials.DM_CHAT_ID + '&parse_mode=Markdown&text=' + \
                bot_message
    response = requests.get(send_text)
    return response.json()


lastUpdate = 0

while True:
    updates = bot.get_updates()

    if len(updates) > lastUpdate and updates[len(updates)-1].message:

        message_text = updates[len(updates)-1].message.text

        print(message_text)
        lastUpdate = len(updates)

        api_result = requests.get(
            'http://api.weatherstack.com/current?access_key=9a2c47630fa21a89a1cd9653c32f7838&query=' + message_text)

        api_response = api_result.json()

        if len(api_response) > 2:
            location = api_response['location']['name']
            current_temperature = api_response['current']['temperature']
            wind_speed = api_response['current']['wind_speed']
            feels_like = api_response['current']['feelslike']

            print(u'Current temperature in %s is %d' % (location, current_temperature))
            bot.send_message(
                chat_id=credentials.DM_CHAT_ID,
                text='Current temperature in ' + location + ' is ' + str(current_temperature) + '\n' +
                     'Feels like ' + str(feels_like) + '\n' +
                     'Wind speed is ' + str(wind_speed) + '\n'
            )
        else:
            print(message_text + " is unknown city name")
            bot.send_message(chat_id=credentials.DM_CHAT_ID, text="Sorry, I don't know that city")

    sleep(3)
