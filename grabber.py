from telethon import TelegramClient, events
import configparser



# тут крч свои данные с my.telegram.org
api_id = 29183638
api_hash = '3a418f74e216f26ef06cab2cfedb67bc'
username = 'WgGlock'

# Переменные каналов
my_channel = -1001869400673
channels = [
    -1001806531947, -1001315411320, -1001499755345, -1001517378907,
    -1001683645732, -1001571533066, -1001105209869, -1001383864679,
    -1001720370296, -1001338316875, -1001154377528
]

# Создание клиента и соединение
client = TelegramClient(username, api_id, api_hash)
print("Граббер - Запущен")

#тут он отправляет
@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        await client.send_message(my_channel, event.message)


client.start()
client.run_until_disconnected()
