# SOURCE https://github.com/Team-ProjectCodeX
# MODULE BY https://t.me/O_okarma
# API BY https://www.github.com/SOME-1HING
# PROVIDED BY https://t.me/ProjectCodeX


import random

import requests
from pyrogram import filters
from pyrogram.types import Message

from REPO import app

API_URL = "https://sugoi-api.vercel.app/news?keyword={}"


@app.on_message(filters.command("news"))
async def news(_, message: Message):
    keyword = (
        message.text.split(" ", 1)[1].strip() if len(message.text.split()) > 1 else ""
    )
    url = API_URL.format(keyword)

    try:
        response = requests.get(url)
        news_data = response.json()

        if "error" in news_data:
            error_message = news_data["error"]
            await message.reply_text(f"Error: {error_message}")
        else:
            if len(news_data) > 0:
                news_item = random.choice(news_data)

                title = news_item["title"]
                excerpt = news_item["excerpt"]
                source = news_item["source"]
                relative_time = news_item["relative_time"]
                news_url = news_item["url"]

                message_text = f"𝗧𝗜𝗧𝗟𝗘: {title}\n𝗦𝗢𝗨𝗥𝗖𝗘: {source}\n𝗧𝗜𝗠𝗘: {relative_time}\n𝗘𝗫𝗖𝗘𝗥𝗣𝗧: {excerpt}\n𝗨𝗥𝗟: {news_url}"
                await message.reply_text(message_text)
            else:
                await message.reply_text("No news found.")

    except requests.exceptions.RequestException as e:
        await message.reply_text(f"Error: {str(e)}")
