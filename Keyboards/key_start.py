from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Handlers.link_photo import  link_google_photo
from Keyboards.callback_datas import BuyCallbackFactory

start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Розбіжності⚠️",
                                 callback_data=BuyCallbackFactory(item_name="choice_discrepancy").pack()
                                 ),
            InlineKeyboardButton(text="Питання по 1С ℹ️",
                                 callback_data=BuyCallbackFactory(item_name="choice_1c_error").pack()
                                 )

        ],
        [
            InlineKeyboardButton(text="Друк документів📝",
                                 callback_data=BuyCallbackFactory(item_name="choice_print").pack()
                                 ),
            InlineKeyboardButton(text="Потоки в 1С📚",
                                 callback_data=BuyCallbackFactory(item_name="choice_ex_imp").pack()
                                 )
        ],
        [
            InlineKeyboardButton(text="Зв'язок з БСЦ📨",
                                 callback_data=BuyCallbackFactory(item_name="choice_contact_bsc").pack()
                                 )
            #,
            #InlineKeyboardButton(text="Файл з інструкцією📥",
            #                     callback_data=BuyCallbackFactory(item_name="choice_contact_bsc").pack()
            #                     , url=link_google_photo + "1tstBKGSZM3t36gqf9K18GxCaXePU-E7K")
        ]
    ]
)
