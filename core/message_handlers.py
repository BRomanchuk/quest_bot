

def init_message_handlers(bot, quest):
    @bot.message_handler(commands=['start', 'help'])
    def start_message(message):
        pass

    @bot.message_handler(commands=['hint'])
    def get_hint(message):
        pass

    @bot.message_handler(commands=['task'])
    def get_task(message):
        pass
