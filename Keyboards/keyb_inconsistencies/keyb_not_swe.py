from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Keyboards.callback_datas import BuyCallbackFactory

inconsis_not_swe = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Списали обладнання в SWE?",
                callback_data=BuyCallbackFactory(item_name="del_swe").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Встановили ТО в мережу КА?",
                callback_data=BuyCallbackFactory(item_name="inst_ka").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Встановили ТО в ТТ іншого складу?",
                callback_data=BuyCallbackFactory(item_name="inst_other").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data=BuyCallbackFactory(item_name="choice_discrepancy").pack()
            ),
            InlineKeyboardButton(
                text="🏠Меню ",
                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
            )
        ]
    ]
)

inconsis_not_swe_ex = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data=BuyCallbackFactory(item_name="not_swe").pack()
            ),
            InlineKeyboardButton(
                text="🏠Меню ",
                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
            )
        ]
    ]
)
