from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Handlers.link_photo import logo_photo, link_google_photo, capex
from Handlers.delete_mes import edit_or_send_message
from Keyboards.callback_datas import BuyCallbackFactory
from Keyboards.keyb_inconsistencies.keyb_not_swe import inconsis_not_swe_ex, inconsis_not_swe

not_swe_router = Router()


@not_swe_router.callback_query(BuyCallbackFactory.filter(F.item_name == "not_swe"))
async def handle_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>Немає В SWE ⛔️</b>",
        photo=logo_photo,
        parse_mode="HTML",
        reply_markup=inconsis_not_swe
    )
    await callback.answer()


@not_swe_router.callback_query(BuyCallbackFactory.filter(F.item_name == "del_swe"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Списали обладнання в SWE?</b>\n"
             "\n"
             "Якщо ТО «Списано» і отримано лист 📩 від БСЦ, необхідно його списати в 1С.\n"
             "Списуємо торгове обладнання по факту відвантаження в ЛОМ. На вкладці "
             "«Звірка залишків» потрібно стати на рядок з ТО, двічі натиснути лівою кнопкою миші,"
             " і першою строкою буде списати обладнання. При натисканні з'явиться заповнена"
             " форма документа «Списания».\n"
             "Далі необхідно натиснути «Провести и закрить».",
        photo=link_google_photo + "1kgO5O0G1KY8cx8G-MXTc0ZjUlaSHC6Wb",
        parse_mode="HTML",
        reply_markup=inconsis_not_swe_ex
    )
    await callback.answer()


@not_swe_router.callback_query(BuyCallbackFactory.filter(F.item_name == "inst_ka"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Встановили ТО в мережу КА?</b>\n"
             "\n"
             "Встановлюючи ТО в мережі КА, відповідальність за обладнання переходить на компанію AB InBev Efes.\n"
             "Відкрий вкладку «Ответственность» і сформуй АПП. Потрібно стати на ТО, двічі натиснути лівою кнопкою миші "
             "у першому рядку обрати «Сформировать Акт приема-передачи», далі натиснути «Провести и закрить».",
        photo=link_google_photo + "1AsZe-h80nvherrYjod4Wycbme0SSjLks",
        parse_mode="HTML",
        reply_markup=inconsis_not_swe_ex
    )
    await callback.answer()


#@not_swe_router.callback_query(BuyCallbackFactory.filter(F.item_name == "inst_other"))
#async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
#    await edit_or_send_message(
#        bot=callback.bot,
#        chat_id=callback.message.chat.id,
#        state=state,
#        text="<b>✅ Встановили ТО в ТТ іншого складу?</b>\n\n"
#             "<b>При встановленні ТО в ТТ змінився склад відповідальний?</b>\n"
#             "Необхідно надати запит на \n"
#             f'👉 {capex}\n'
#             "який склад фактично відповідальний за ТО.",
#        photo=link_google_photo + "1DW0iX5US4UyewmJnOx5fRxZOlk-EJqoz",
#        parse_mode="HTML",
#        reply_markup=inconsis_not_swe_ex
#    )
#    await callback.answer()
