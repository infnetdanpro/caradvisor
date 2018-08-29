import logging
import datetime
import requests

from settings import TELEGRAM_API_KEY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from get_weather import get_current_weather_message, get_weather_forecast_for_six_hours
from roads_closed import get_road_restrictions
from predict_traffic import get_jams, get_jam_level, get_jams_icon_color, day_type, predict_function, predict_stat


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    # filename='bot.log'
                    )


def caradvice(bot, update):
    caradvisor_weather_message = get_current_weather_message()
    caradvisor_weather_forecast_six_hours_message = get_weather_forecast_for_six_hours()

    cardvisor_traffic_jam_message = get_jams() + ': пробки ' + get_jam_level() + ' балла'
    cardvisor_traffic_jam_message += ' (' + get_jams_icon_color() + ') '
    jam_prediction_six_hours_ahead = predict_function(predict_stat, predict_start=3, predict_end=12, predict_step=3)
    jam_prediction_by_day_type_message = day_type()

    update.message.reply_text(caradvisor_weather_message)
    update.message.reply_text(caradvisor_weather_forecast_six_hours_message)

    update.message.reply_text(cardvisor_traffic_jam_message)
    update.message.reply_text(jam_prediction_six_hours_ahead)
    update.message.reply_text(jam_prediction_by_day_type_message)
    update.message.reply_photo('http://static-maps.yandex.ru/1.x/?ll=37.620070,55.753630&spn=0.34,0.34&l=map,trf') #caption='Карта пробок'


def closed_roads(bot, update):
    caradvisor_closed_roads_message = get_road_restrictions()

    update.message.reply_text(caradvisor_closed_roads_message)


def chat(bot, update):
    text = update.message.text
    logging.info(text)

    update.message.reply_text('Hello!')


def main():
    upd = Updater(TELEGRAM_API_KEY)

    upd.dispatcher.add_handler(CommandHandler('caradvice', caradvice))
    upd.dispatcher.add_handler(CommandHandler('closed_roads', closed_roads))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    upd.start_polling()
    upd.idle()


if __name__ == '__main__':
    logging.info('Bot started')
    main()
