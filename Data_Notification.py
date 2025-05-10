import telegram
import asyncio

# Telegram Bot Setup
BOT_TOKEN = "8195476558:AAHaeoyfz2nZStVHfbwBaDwA5nZqAyUB8xg"
CHAT_ID = "1697253014"

async def send_telegram_notification(message):
    try:
        bot = telegram.Bot(token=BOT_TOKEN)
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print('Telegram Message Sent')
    except Exception as e:
        print(f"Telegram Error: {e}")
async def check_fall():
    file2 = open("Data2.txt", "r")
    if file2.read() == "FALL DETECTED":
        print("FALL DETECTED")
        await send_telegram_notification("FALL DETECTED")
        file2 = open("Data2.txt", "w")
        file2.write(" ")
async def check_out():
    file1 = open("Data1.txt", "r")
    if file1.read() == "OUT OF FOCUS":
        print("OUT OF FOCUS")
        await send_telegram_notification("OUT OF FOCUS")
        file1 = open("Data1.txt", "w")
        file1.write(" ")
async def main():
    while True:
        await check_out()
        await check_fall()

if __name__ == '__main__':
    asyncio.run(main())
