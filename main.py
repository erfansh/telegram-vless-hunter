from telethon import TelegramClient
import re
from config import api_id, api_hash, channels
import asyncio

vless_pattern = re.compile(r'vless://[^\s]+')

async def main():
    client = TelegramClient('session_session', api_id, api_hash)
    await client.start()
    print("✅ Connected to Telegram.")

    found_links = set()

    for channel in channels:
        print(f"🔍 Reading channel: {channel}")
        try:
            async for message in client.iter_messages(channel, limit=100):
                if message.message:
                    matches = vless_pattern.findall(message.message)
                    found_links.update(matches)
        except Exception as e:
            print(f"⚠️ Error in channel {channel}: {e}")

    print(f"🔗 Found {len(found_links)} VLESS links.")

    # نوشتن در فایل sub.txt
    with open('sub.txt', 'w', encoding='utf-8') as f:
        for link in found_links:
            f.write(link + '\n')

    print("📁 sub.txt آماده شد.")
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
