from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Keyboards.callback_datas import BuyCallbackFactory

print_add_rep_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        # [
        #    InlineKeyboardButton(
        #        text="Крок 2 →",
        #        callback_data=BuyCallbackFactory(item_name="add_rep_2").pack()
        #    ),
        #    InlineKeyboardButton(
        #        text="Крок 3 →→",
        #        callback_data=BuyCallbackFactory(item_name="add_rep_3").pack()
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

# print_add_rep_2 = InlineKeyboardMarkup(
#    inline_keyboard=[
#        [
#            InlineKeyboardButton(
#                text="← Крок 1",
#                callback_data=BuyCallbackFactory(item_name="pdck_add_rep_info").pack()
#            ),
#            InlineKeyboardButton(
#                text="Крок 3 →",
#                callback_data=BuyCallbackFactory(item_name="add_rep_3").pack()
#            )
#        ],
#        [
#            InlineKeyboardButton(
#                text="🔙 Назад",
#                callback_data=BuyCallbackFactory(item_name="choice_print").pack()
#            ),
#           InlineKeyboardButton(
#                text="🏠Меню ",
#                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
#            )
#        ]
#    ]
# )
#
# print_add_rep_3 = InlineKeyboardMarkup(
#    inline_keyboard=[
#        [
#            InlineKeyboardButton(
#                text="←← Крок 1",
#                callback_data=BuyCallbackFactory(item_name="pdck_add_rep_info").pack()
#            ),
#            InlineKeyboardButton(
#                text="← Крок 2",
#                callback_data=BuyCallbackFactory(item_name="add_rep_2").pack()
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
