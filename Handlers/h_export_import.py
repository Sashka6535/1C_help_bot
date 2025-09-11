from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Handlers.link_photo import logo_photo, link_google_photo
from Handlers.delete_mes import edit_or_send_message
from Keyboards.callback_datas import BuyCallbackFactory
from Keyboards.expotr_import import export_import, export_import_ex
from Keyboards.keyb_inconsistencies.keyb_not_swe import inconsis_not_swe_ex, inconsis_not_swe

exoprtimport_router = Router()


@exoprtimport_router.callback_query(BuyCallbackFactory.filter(F.item_name == "choice_ex_imp"))
async def handle_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>Обери необхідну для тебе дію</b>",
        photo=logo_photo,
        parse_mode="HTML",
        reply_markup=export_import
    )
    await callback.answer()


@exoprtimport_router.callback_query(BuyCallbackFactory.filter(F.item_name == "eximp_to1C"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Завантажити дані в 1С?</b>\n"
             "\n"
             "Для початку роботи з ТО оператору необхідно запустити інтерфейс — файл CASInterface.epf.\n"
             "У результаті з’явиться вікно Робоче місце оператора ➡️ Обладнання ➡️ Завантажити дані в 1С.\n\n"
             "Для завантаження даних на відкритій формі обираємо Точку Синхронізації та натискаємо кнопку «Завантажити».",
        photo=link_google_photo + "1zD6JtolKDYqVJcHCdGxDOgaAXXJhSj0Q",
        parse_mode="HTML",
        reply_markup=export_import_ex
    )
    await callback.answer()


@exoprtimport_router.callback_query(BuyCallbackFactory.filter(F.item_name == "eximp_from1C"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Вивантажити дані з 1С?</b>\n"
             "\n"
             "Для початку роботи з ТО оператору необхідно запустити інтерфейс — файл CASInterface.epf.\n"
             "У результаті з’явиться вікно Робоче місце оператора ➡️ Вивантажити дані в 1С ➡️ Вивантажити.",
        photo=link_google_photo + "16z-4iWySPCdR0C-Y7E09cK2_Jh8TZ85s",
        parse_mode="HTML",
        reply_markup=export_import_ex
    )
    await callback.answer()


@exoprtimport_router.callback_query(BuyCallbackFactory.filter(F.item_name == "eximp_db"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        # текст станет caption для фото
        text=(
            "<b>✅ Вивантажити базу ТО?</b>\n\n"
            "Звіт «Звірка залишків» ➡️ Залишки1С ➡️ Файл ➡️ Зберегти як, обрати формат Excel.\n\n"
            "⚠️ Якщо у вас немає доступу для збереження, необхідно звернутися до вашого програміста."
        ),
        photo=link_google_photo + "128DTj4T19e9q9BkOjRwEu94IFY9XsdD3",
        parse_mode="HTML",
        reply_markup=export_import_ex
    )
    await callback.answer()
