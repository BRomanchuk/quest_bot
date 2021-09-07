from flask import Flask
import telebot

from core.routes import init_routes
from core.message_handlers import init_message_handlers

from structure.quest import Quest

from settings.constants import TOKEN

bot = telebot.TeleBot(TOKEN)
quest = Quest('quest_name_here')


def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_routes(app, bot)
        init_message_handlers(bot, quest)
        return app
