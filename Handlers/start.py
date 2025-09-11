from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Handlers.delete_mes import edit_or_send_message
from Handlers.link_photo import logo_photo
from Handlers.questions.h_errors import errors_router
from Handlers.h_call_to_bsc import callbsc_router
from Handlers.h_export_import import exoprtimport_router
from Handlers.inconsistencies import invcons_router
from Handlers.print_dock import printdock_router

from Keyboards.callback_datas import BuyCallbackFactory
from Keyboards.key_start import start_menu

main_router = Router()

main_router.include_routers(invcons_router, printdock_router, errors_router, callbsc_router, exoprtimport_router)


# 📌 Стартовое сообщение
@main_router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    try:
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception:
        pass

    data = await state.get_data()

    # Удаляем старые сообщения от бота
    for key in ["first_message_id"]:
        msg_id = data.get(key)
        if msg_id:
            try:
                await message.bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
            except Exception:
                pass

    # Отправляем приветственное сообщение
    msg = await message.answer_photo(
        photo=logo_photo,
        caption=(
            "<b>Привіт!✌️</b>\n"
            "Я твій бот підтримки🤖\n"
            "Відповім на питання по розбіжностям між 1С💻 та SWE🖥️,\n"
            "підкажу, як сформувати та роздрукувати документи 🧾\n"
            "та до кого звернутися, якщо моїх знань буде недостатньо👩‍🎓."
        ),
        parse_mode="HTML",
        reply_markup=start_menu
    )

    await state.update_data({
        "first_message_id": msg.message_id,
        "started": True
    })


# 🧹 Удаление любого текста от пользователя
@main_router.message(F.text)
async def delete_unwanted_text(message: Message):
    try:
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception:
        pass


# 🔄 Обработка inline-кнопок
@main_router.callback_query(BuyCallbackFactory.filter(F.item_name == "choice_menu"))
async def handle_choice_discrepancy(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        photo=logo_photo,
        text=(
            "<b>Привіт!✌️</b>\n"
            "Я твій бот підтримки🤖\n"
            "Відповім на питання по розбіжностям між 1С💻 та SWE🖥️,\n"
            "підкажу, як сформувати та роздрукувати документи 🧾\n"
            "та до кого звернутися, якщо моїх знань буде недостатньо👩‍🎓."),
        parse_mode="HTML",
        reply_markup=start_menu
    )
    await callback.answer()
