from settings.message_processor import get_start_message, get_hint, get_current_task, process_text


def init_message_handlers(bot, quest):
    @bot.message_handler(commands=['start', 'help'])
    def start_message(message):
        get_start_message(bot, message, quest)

    @bot.message_handler(commands=['hint'])
    def hint(message):
        get_hint(bot, message, quest)

    @bot.message_handler(commands=['task'])
    def current_task(message):
        get_current_task(bot, message, quest)

    @bot.message_handler(content_types=['text'])
    def text(message):
        process_text(bot, message, quest)

