# SOURCE https://github.com/Team-ProjectCodeX
# MODULE BY https://t.me/O_okarma
# API BY https://www.github.com/SOME-1HING
# PROVIDED BY https://t.me/ProjectCodeX


import random

import requests
from telegram import Update
from telegram.ext import CommandHandler

from REPO import dispatcher

API_URL = "https://sugoi-api.vercel.app/news?keyword={}"


def news(update: Update, context):
    keyword = context.args[0] if context.args else ""
    url = API_URL.format(keyword)

    try:
        response = requests.get(url)
        news_data = response.json()

        if "error" in news_data:
            error_message = news_data["error"]
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=f"Error: {error_message}"
            )
        else:
            if len(news_data) > 0:
                # Randomly select a news item from the list
                news_item = random.choice(news_data)

                title = news_item["title"]
                excerpt = news_item["excerpt"]
                source = news_item["source"]
                relative_time = news_item["relative_time"]
                news_url = news_item["url"]

                message = f"𝗧𝗜𝗧𝗟𝗘: {title}\n𝗦𝗢𝗨𝗥𝗖𝗘: {source}\n𝗧𝗜𝗠𝗘: {relative_time}\n𝗘𝗫𝗖𝗘𝗥𝗣𝗧: {excerpt}\n𝗨𝗥𝗟: {news_url}"
                context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            else:
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text="No news found."
                )

    except requests.exceptions.RequestException as e:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f"Error: {str(e)}"
        )


news_handler = CommandHandler("news", news)
dispatcher.add_handler(news_handler)
