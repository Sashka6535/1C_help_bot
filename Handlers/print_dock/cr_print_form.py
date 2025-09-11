from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Handlers.delete_mes import edit_or_send_message
from Handlers.link_photo import link_google_photo
from Keyboards.callback_datas import BuyCallbackFactory
from Keyboards.keyb_print_dock.key_creat_print_form import cr_pr_fm_1

cr_print_file = Router()


@cr_print_file.callback_query(BuyCallbackFactory.filter(F.item_name == "pdck_var_pr_dock"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Cформувати друковану форму з заявки?</b>\n\n"
             "Для підписання договору про передачу або прийняття "
             "обладнання необхідно сформувати та роздрукувати документ для"
             " передачі на підпис торговій команді. Виконай дії, котрі "
             "зображені на схемі та перевір коректність даних.",
        photo=link_google_photo + "1evWoINPQCcpqiL_7xLlFLkDwnbdCze6-",
        parse_mode="HTML",
        reply_markup=cr_pr_fm_1
    )
    await callback.answer()


@cr_print_file.callback_query(BuyCallbackFactory.filter(F.item_name == "pdck_cr_pr_form"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Cформувати друковану форму з «Сверка остатков»</b>\n\n"
             "Для підписання договору про передачу або прийняття "
             "обладнання необхідно сформувати та роздрукувати документ для"
             " передачі на підпис торговій команді. Виконай дії, котрі "
             "зображені на схемі та перевір коректність даних.",
        photo=link_google_photo + "1qErx8xv8LQ4R80p2J9rLEtL3ZKEAEc_P",
        parse_mode="HTML",
        reply_markup=cr_pr_fm_1
    )
    await callback.answer()
