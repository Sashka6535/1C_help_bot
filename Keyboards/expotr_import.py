from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Keyboards.callback_datas import BuyCallbackFactory

export_import = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Завантажити дані в 1С?",
                callback_data=BuyCallbackFactory(item_name="eximp_to1C").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Вивантажити дані з 1С?",
                callback_data=BuyCallbackFactory(item_name="eximp_from1C").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Вивантажити базу ТО?",
                callback_data=BuyCallbackFactory(item_name="eximp_db").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
            )
        ]
    ]
)

export_import_ex = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data=BuyCallbackFactory(item_name="choice_ex_imp").pack()
            )
        ]
    ]
)
