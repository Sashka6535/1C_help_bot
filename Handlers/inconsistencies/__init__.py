from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Handlers.link_photo import logo_photo
from Handlers.delete_mes import edit_or_send_message
from Handlers.inconsistencies.incons_not_swe import not_swe_router
from Handlers.inconsistencies.invons_location import location_router
from Handlers.inconsistencies.invons_not_osd import not_osd_router
from Keyboards.callback_datas import BuyCallbackFactory
from Keyboards.keyb_inconsistencies.keyb_incons import menu_inconsist

invcons_router = Router()

invcons_router.include_routers(not_swe_router, not_osd_router, location_router)


# 🔄 Обработка inline-кнопок
@invcons_router.callback_query(BuyCallbackFactory.filter(F.item_name == "choice_discrepancy"))
async def handle_choice_discrepancy(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>Обери необхідний тип розбіжностей⚠️</b>",
        photo=logo_photo,
        parse_mode="HTML",
        reply_markup=menu_inconsist
    )
    await callback.answer()
