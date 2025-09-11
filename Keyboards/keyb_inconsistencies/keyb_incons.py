from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Keyboards.callback_datas import BuyCallbackFactory

menu_inconsist = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Немає В SWE ⛔️",
                callback_data=BuyCallbackFactory(item_name="not_swe").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Немає в ОСД ⭕️",
                callback_data=BuyCallbackFactory(item_name="no_osd").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Відрізняється локація ❌",
                callback_data=BuyCallbackFactory(item_name="no_lock").pack()
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