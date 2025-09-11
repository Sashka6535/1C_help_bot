from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Keyboards.callback_datas import BuyCallbackFactory

errors_keyboard = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Технічна помилка?",
                callback_data=BuyCallbackFactory(item_name="errors_tech").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Декілька документів на 1 ТО?",
                callback_data=BuyCallbackFactory(item_name="errors_few_dock").pack()
            )
        ],
        #[
        #    InlineKeyboardButton(
        #       text="Не вдається заблокувати запис?",
    #       callback_data=BuyCallbackFactory(item_name="errors_no_record").pack()
        #       )
        #],
        [
            InlineKeyboardButton(
                text="Не вдається провести заявку?",
                callback_data=BuyCallbackFactory(item_name="errors_no_req").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Додати обладнання в групове переміщення?",
                callback_data=BuyCallbackFactory(item_name="errors_add_equip_s1").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Пусті поля в заявці?",
                callback_data=BuyCallbackFactory(item_name="errors_field_req").pack()
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

errors_keyboard_st1_ex = InlineKeyboardMarkup(
    inline_keyboard=[
        #[
        #    InlineKeyboardButton(
        #        text="Крок 2 →",
        #        callback_data=BuyCallbackFactory(item_name="errors_add_equip_s2").pack()
        #    ),
        #    InlineKeyboardButton(
        #        text="Крок 3 →→",
        #        callback_data=BuyCallbackFactory(item_name="errors_add_equip_s3").pack()
        #    )
        #],
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data=BuyCallbackFactory(item_name="choice_1c_error").pack()
            ),
            InlineKeyboardButton(
                text="🏠Меню ",
                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
            )
        ]
    ]
)

#errors_keyboard_st2_ex = InlineKeyboardMarkup(
#    inline_keyboard=[
#        [
#            InlineKeyboardButton(
#                text="← Крок 1",
#                callback_data=BuyCallbackFactory(item_name="errors_add_equip_s1").pack()
#            ),
#            InlineKeyboardButton(
#                text="Крок 3 →",
#                callback_data=BuyCallbackFactory(item_name="errors_add_equip_s3").pack()
#            )
#        ],
#        [
#            InlineKeyboardButton(
#                text="🔙 Назад",
#                callback_data=BuyCallbackFactory(item_name="choice_1c_error").pack()
#            ),
#            InlineKeyboardButton(
#                text="🏠Меню ",
#                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
#            )
#        ]
#    ]
#)

#errors_keyboard_st3_ex = InlineKeyboardMarkup(
#    inline_keyboard=[
#        [
#            InlineKeyboardButton(
#                text="←← Крок 1",
#                callback_data=BuyCallbackFactory(item_name="errors_add_equip_s1").pack()
#            ),
#            InlineKeyboardButton(
#                text="← Крок 2",
#                callback_data=BuyCallbackFactory(item_name="errors_add_equip_s2").pack()
#            )
#        ],
#        [
#            InlineKeyboardButton(
#                text="🔙 Назад",
#                callback_data=BuyCallbackFactory(item_name="choice_1c_error").pack()
#            ),
#            InlineKeyboardButton(
#                text="🏠Меню ",
#                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
#            )
#        ]
#    ]
#)

errors_keyboard_ex = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data=BuyCallbackFactory(item_name="choice_1c_error").pack()
            ),
            InlineKeyboardButton(
                text="🏠Меню ",
                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
            )
        ]
    ]
)