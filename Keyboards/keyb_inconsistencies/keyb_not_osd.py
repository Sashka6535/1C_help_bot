from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Keyboards.callback_datas import BuyCallbackFactory

inconsis_not_osd = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Списали не те обладнання?",
                callback_data=BuyCallbackFactory(item_name="osd_delswe").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="З'явилось в 1С не твоє обладнання?",
                callback_data=BuyCallbackFactory(item_name="osd_noknow_to").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="З'явилось ТО з мережі КА?",
                callback_data=BuyCallbackFactory(item_name="osd_to_ka").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Висить розбіжність зі статусом ""Отгружено""?",
                callback_data=BuyCallbackFactory(item_name="osd_otgruz").pack()
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

inconsis_not_osd_ex = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data=BuyCallbackFactory(item_name="no_osd").pack()
            ),
            InlineKeyboardButton(
                text="🏠Меню ",
                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
            )
        ]
    ]
)
