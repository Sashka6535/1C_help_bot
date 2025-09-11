from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Keyboards.callback_datas import BuyCallbackFactory

menu_print_dock = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Корегування довідкової інформації",
                callback_data=BuyCallbackFactory(item_name="pdck_add_rep_info").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Друк з «Документы по оборудованию»",
                callback_data=BuyCallbackFactory(item_name="pdck_var_pr_dock").pack()
            )
        ],
        [
            InlineKeyboardButton(
                text="Друк з «Сверка остатков»",
                callback_data=BuyCallbackFactory(item_name="pdck_cr_pr_form").pack()
            )
        ],
        # [
        #    InlineKeyboardButton(
        #        text="Формування друкованої форми з заявки",
        #        callback_data=BuyCallbackFactory(item_name="pdck_var_pr_dock").pack()
        #    )
        # ],
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data=BuyCallbackFactory(item_name="choice_menu").pack()
            )
        ]
    ]
)

var_pr_dc1 = InlineKeyboardMarkup(
    inline_keyboard=[
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
