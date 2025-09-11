from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Keyboards.callback_datas import BuyCallbackFactory

cr_pr_fm_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        # [
        #    InlineKeyboardButton(
        #        text="Крок 2 →",
        #        callback_data=BuyCallbackFactory(item_name="cr_pr_2").pack()
        #    )
        # ],
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data=BuyCallbackFactory(item_name="choice_print").pack()
            ),
            InlineKeyboardButton(
                text="🏠Меню ",
                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
            )
        ]
    ]
)

# cr_pr_fm_2 = InlineKeyboardMarkup(
#    inline_keyboard=[
#        [
#            InlineKeyboardButton(
#                text="← Крок 1",
#                callback_data=BuyCallbackFactory(item_name="pdck_cr_pr_form").pack()
#            )
#        ],
#        [
#            InlineKeyboardButton(
#                text="🔙 Назад",
#                callback_data=BuyCallbackFactory(item_name="choice_print").pack()
#            ),
#            InlineKeyboardButton(
#                text="🏠Меню ",
#                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
#            )
#        ]
#    ]
# )
