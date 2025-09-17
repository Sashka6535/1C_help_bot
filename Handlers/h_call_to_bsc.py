from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Handlers.link_photo import logo_photo, capex, coolers, issuppor
from Handlers.delete_mes import edit_or_send_message
from Keyboards.callback_datas import BuyCallbackFactory
from Keyboards.callbsc import callbsc

callbsc_router = Router()


@callbsc_router.callback_query(BuyCallbackFactory.filter(F.item_name == "choice_contact_bsc"))
async def handle_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>Зв'язок з БСЦ</b>\n\n"
             "<b>Оберіть необхідну пошту:</b>\n\n"
             "По питанням автообміну, КПІ, стратегії вивозу обладнання:\n"
             f"👉  {capex}; \n\n"
             "По питанням складської інвентаризації, виведення з втрат, комплектуючих, ремонтів:\n"
             f"👉 {coolers}; \n\n"
             "По питанням технічних помилок на боці 1С:\n"
             f"👉 {issuppor}. \n",
        photo=logo_photo,
        parse_mode="HTML",
        reply_markup=callbsc
    )
    await callback.answer()
