from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Keyboards.callback_datas import BuyCallbackFactory

inconsis_reloc = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Не проводиться заявка через тех. стан ТО?",
                callback_data=BuyCallbackFactory(item_name="reloc_req_tehcond").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Зависла виконана заявка в системі?",
                callback_data=BuyCallbackFactory(item_name="reloc_req_done").pack()
            )
        ],
#        [
#            InlineKeyboardButton(
#                text="Потрібно провести ручну заявку?",
#                callback_data=BuyCallbackFactory(item_name="reloc_osd").pack()
#            )
#        ],
        [
            InlineKeyboardButton(
                text="Провели заявки в період інвентаризації?",
                callback_data=BuyCallbackFactory(item_name="reloc_req_inv").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Виникла розбіжність через перейменування ТТ?",
                callback_data=BuyCallbackFactory(item_name="reloc_rename_tt").pack()
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

inconsis_reloc_ex = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data=BuyCallbackFactory(item_name="no_lock").pack()
            ),
            InlineKeyboardButton(
                text="🏠Меню ",
                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
            )
        ]
    ]
)
