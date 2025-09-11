from aiogram.filters.callback_data import CallbackData


class BuyCallbackFactory(CallbackData, prefix="buy"):
    item_name: str
