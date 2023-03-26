import psutil
import telebot

TOKEN = '5837701589:AAHLWwlqe9tHIQwcpE5ua6wM6cHcgKx0hKM'
CHAT_ID = '5837701589'
RAM_THRESHOLD = 80 
CPU_THRESHOLD = 80 
MEMORY_THRESHOLD = 80  

bot = telebot.TeleBot(TOKEN)

def send_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

def monitor():
    cpu_percent = psutil.cpu_percent()
    ram_percent = psutil.virtual_memory().percent
    memory_percent = psutil.disk_usage('/').percent

    if ram_percent > RAM_THRESHOLD:
        message = f'🔴 WARNING! RAM usage is overload on {ram_percent}%.'
        send_message(message)

    if cpu_percent > CPU_THRESHOLD:
        message = f'🔴 WARNING! CPU usage is overload on {cpu_percent}%.'
        send_message(message)

    if memory_percent > MEMORY_THRESHOLD:
        message = f'🔴 WARNING! memory usage is overload on {memory_percent}%.'
        send_message(message)

while True:
    monitor()
    time.sleep(300)