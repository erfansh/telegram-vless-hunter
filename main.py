import asyncio
import re
from telethon import TelegramClient
from config import api_id, api_hash, channels

# الگوی دقیق‌تر برای شناسایی لینک vless
vless_pattern = re.compile(r'vless://[^\s]+')

async def main():
    client = TelegramClient('session_session', api_id, api_hash)
    await client.start()
    print("🚀 Connected to Telegram!")

    for channel in channels:
        print(f"📡 Reading channel: {channel}")
        try:
            async for message in client.iter_messages(channel, limit=100):
                if message.message:
                    matches = vless_pattern.findall(message.message)
                    for match in matches:
                        print(f"🔹 Found vless config: {match}")
        except Exception as e:
            print(f"⚠️ Error reading channel {channel}: {e}")

    print("🏁 Task completed.")
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
