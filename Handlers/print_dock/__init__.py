from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Handlers.link_photo import logo_photo
from Handlers.delete_mes import edit_or_send_message
from Handlers.print_dock.add_rep_info import add_rep_info_router
from Handlers.print_dock.cr_print_form import cr_print_file
from Keyboards.callback_datas import BuyCallbackFactory
from Keyboards.keyb_print_dock.key_print_dock import menu_print_dock

printdock_router = Router()

printdock_router.include_routers(add_rep_info_router, cr_print_file)

@printdock_router.callback_query(BuyCallbackFactory.filter(F.item_name == "choice_print"))
async def handle_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="Друк документів📝",
        photo=logo_photo,
        parse_mode="HTML",
        reply_markup=menu_print_dock
    )
    await callback.answer()