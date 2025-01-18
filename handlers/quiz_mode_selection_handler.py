from config import bot
from utils import main_function
from utils.vocabulary_functions import selecting_mode
from utils.main_function import main_menu_markup


def register_quiz_mode_selection_handler():
    @bot.callback_query_handler(func=lambda callback: 'mode' in callback.data)
    def callback_quiz_mode_selection(callback):
        callback.data = callback.data[-1]
        print('im here')

        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        # main_function.main_menu_markup(callback.message)
        selecting_mode(message=callback.data, returned_main_menu=main_menu_markup)

