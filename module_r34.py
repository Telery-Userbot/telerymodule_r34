from pyrogram import Client, filters
import requests

with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()

cinfo = f"`{prefix_userbot}r34`"
ccomand = " ищет hentai-фото"


def command_r34(app):
    @app.on_message(filters.me & filters.command("r34", prefixes=prefix_userbot))
    def r34_module(_, message):
        try:
            query = message.text.split(" ", 2)[1:]
            if len(query) == 0:
                message.edit("Пожалуйста, укажите запрос.")
                return
            search_term = query[0]
            image_number = int(query[1]) if len(query) > 1 else 1
            search_url = f"https://nhentai.net/api/galleries/search?query={search_term}"
            response = requests.get(search_url)
            if response.status_code != 200:
                message.edit("Ошибка при поиске на NHentai.")
                return
            results = response.json().get('result', [])
            if not results:
                message.edit(f"Ничего не найдено по запросу: {search_term}")
                return
            if image_number > len(results) or image_number < 1:
                message.edit(f"Недопустимый номер фото: {image_number}")
                return
            doujinshi = results[image_number - 1]
            cover_url = f"https://t.nhentai.net/galleries/{doujinshi['media_id']}/cover.jpg"
            if cover_url:
                message.reply_photo(photo=cover_url)
            else:
                message.edit("Фото не найдено.")
        except Exception as e:
            message.edit(f"Ошибка: {str(e)}")

print("Модуль r34 загружен!")
