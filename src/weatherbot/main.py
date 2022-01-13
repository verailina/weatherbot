import logging
import math
from pathlib import Path
from typing import Tuple

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler

from weatherbot.weather import get_weather_forecast, parse_weather_forecast
from weatherbot.visualization import get_weather_image

def get_token() -> str:
    with Path("bottoken.txt").open() as token_file:
        token = token_file.readline()

    return token


updater = Updater(token=get_token(), use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")


def show_weather(update, context):
    forecast = get_weather_forecast()
    weather_points = parse_weather_forecast(forecast)

    def get_data(point) -> Tuple[str, str, str]:
        date_row = point.date.strftime("%H:%M")
        temperature = int(point.temperature)
        if (point.temperature - temperature) > 0.5:
            temperature = math.ceil(point.temperature)
        return date_row, point.temperature, str(temperature)

    data = [get_data(x) for x in weather_points]
    print(*list(zip(*data)))
    print(weather_points)
    weather_image = get_weather_image(weather_points)

    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=weather_image)


# def inline_caps(update, context):
#     query = update.inline_query.query
#     if not query:
#         return
#     results = list()
#     results.append(
#         InlineQueryResultArticle(
#             id=query.upper(),
#             title='Note',
#             input_message_content=InputTextMessageContent(query)
#         )
#     )
#     save_note(query)
#     context.bot.answer_inline_query(update.inline_query.id, results)
#
#
# inline_caps_handler = InlineQueryHandler(inline_caps, run_async=True)
# dispatcher.add_handler(inline_caps_handler)



start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

weather_handler = CommandHandler('weather', show_weather)
dispatcher.add_handler(weather_handler)

#
# def caps(update, context):
#     text_caps = ' '.join(context.args).upper()
#     context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
#
#
# def note(update, context):
#     print(context.args)
#
#
#
#
# caps_handler = CommandHandler('caps', caps)
# dispatcher.add_handler(caps_handler)
# dispatcher.add_handler(CommandHandler("note", note))

updater.start_polling()
