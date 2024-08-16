# Імпортувати до проєкту бібліотеку Telethon (або аналогічні) та інші необхідні модулі за зразками з лекції 11.
from telethon.sync import TelegramClient
from pytz import timezone
import re

# Зареєструватись на сторінці для розробників Telegram: my.telegram.org/apps
api_id = ###
api_hash = ###

# Створити та запустити клієнт для з’єднання з Telegram, використовуючи вищезазначені параметри, а також свій username та/або номер телефону.
# Пройти авторизацію при першому запуску клієнта для збереження сесії.
client = TelegramClient('session_name', api_id, api_hash)
client.start()

# Створити в Telegram власний публічний канал із довільним нікнеймом.
# Наповнити канал приблизно 10 постами з довільним текстом, обсяг кожного — один абзац на 20–40 слів.
# Під’єднатись до свого каналу з Python (чи іншої мови програмування), зчитати та вивести в консоль його ID, username, назву (заголовок), дату створення.

channel_name = "@lab_6_api"
Channel = client.get_entity(channel_name)

local_tz = timezone('Europe/Kiev')

print("-----Інформація про канал-----")
print(f"ID: {Channel.id}, "
      f"Username: {Channel.username}, "
      f"Назва: {Channel.title}, "
      f"Дата створення: {Channel.date.astimezone(local_tz)}")

# Зчитати з каналу 4 пости (останні), і для кожного з них вивести в консоль:
# дату й час публікації;
# зміст (текст);
# кількість знаків (символів);
# кількість слів.
# Завдання на максимальний бал: при виведенні часу публікації постів привести його до часового поясу Києва.

all_msgs = client.iter_messages(Channel)

print('-'*20)

for i, message in enumerate(all_msgs):
    print(f"Номер повідомлення: {i+1}")
    print(f"Дата й час публікації: {message.date.astimezone(local_tz)}")
    if message.message:
        text = message.message
        print(f"Зміст: {text}")
        print(f"""Кількість слів: {len(re.findall("[А-ЩЬЮЯҐЄІЇа-щьюяґєії'`’ʼ-]+", text))}""")
        print(f"Кількість знаків: {len(text)}")
        print('-' * 20)
    else:
        print(f"Зміст: порожнє повідомлення")

print('-' * 20)
print(f"Загальна кількість постів на каналі: {client.get_messages(Channel).total}")

with open('lab6_all_messages.txt', encoding="utf-8", mode='a') as f:
    for message in all_msgs:
        if message.message:
            f.write(message.date.astimezone(local_tz).strftime("%d-%b-%Y, %H:%M:%S   "))
            f.write(message.message)
            f.write('\n\n')
        else:
            f.write(message.date.astimezone(local_tz).strftime("%d-%b-%Y, %H:%M:%S   "))
            f.write('Порожнє повідомлення')
            f.write('\n\n')