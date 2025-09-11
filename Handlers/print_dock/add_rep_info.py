from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Handlers.delete_mes import edit_or_send_message
from Handlers.link_photo import link_google_photo
from Keyboards.callback_datas import BuyCallbackFactory
from Keyboards.keyb_print_dock.key_add_rep_info import print_add_rep_1  # , print_add_rep_2, print_add_rep_3

add_rep_info_router = Router()


@add_rep_info_router.callback_query(BuyCallbackFactory.filter(F.item_name == "pdck_add_rep_info"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Скорегувати довідкову інформацію?</b>\n\n"
        # "<b>Крок 1:</b>\n\n"
             "На головній сторінці 1С натиснути кнопку «Операции»→«Справочник»→"
             "«ABI POS Подразделения»→Обираєте свій склад→Стати на поле,"
             " яке необхідно скорегувати→в лівому верхньому куту натиснути «Изменить»",
        photo= link_google_photo + "1qsycPc09KtuChjcg0huNH9-asPt91ynU",
        parse_mode="HTML",
        reply_markup=print_add_rep_1
    )
    await callback.answer()

# @add_rep_info_router.callback_query(BuyCallbackFactory.filter(F.item_name == "add_rep_2"))
# async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
#    await edit_or_send_message(
#        bot=callback.bot,
#        chat_id=callback.message.chat.id,
#        state=state,
#        text="<b>✅ Скорегувати довідкову інформацію?</b>\n\n"
#             "<b>Крок 2:</b>\n\n"
#             "В новому вікні обери «ABI POS Подразделения» і далі  «ОК»✔️",
#        photo="https://drive.google.com/uc?export=download&id=1aIXYLaMfBNYVz8UCH81pFVjJKOCvrb-4",
#        parse_mode="HTML",
#        reply_markup=print_add_rep_2
#    )
#    await callback.answer()


# @add_rep_info_router.callback_query(BuyCallbackFactory.filter(F.item_name == "add_rep_3"))
# async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
#    await edit_or_send_message(
#        bot=callback.bot,
#        chat_id=callback.message.chat.id,
#        state=state,
#        text="<b>✅ Скорегувати довідкову інформацію?</b>\n\n"
#             "<b>Крок 3:</b>\n",
#        photo="https://drive.google.com/uc?export=download&id=1J9TI1zDQruEMFxwRS1rSj1en3ri5QihD",
#        parse_mode="HTML",
#        reply_markup=print_add_rep_3
#    )
#    await callback.answer()
