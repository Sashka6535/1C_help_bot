from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Keyboards.callback_datas import BuyCallbackFactory

callbsc = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
            )
        ]
    ]
)
