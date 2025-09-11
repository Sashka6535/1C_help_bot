from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Handlers.link_photo import logo_photo, link_google_photo, capex, coolers
from Handlers.delete_mes import edit_or_send_message
from Keyboards.callback_datas import BuyCallbackFactory
from Keyboards.errors.key_errors import errors_keyboard, errors_keyboard_ex, errors_keyboard_st1_ex

errors_router = Router()


@errors_router.callback_query(BuyCallbackFactory.filter(F.item_name == "choice_1c_error"))
async def handle_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>Питання по 1Сℹ️</b>",
        photo=logo_photo,
        parse_mode="HTML",
        reply_markup=errors_keyboard,
    )
    await callback.answer()


@errors_router.callback_query(BuyCallbackFactory.filter(F.item_name == "errors_tech"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Технічна помилка?</b>\n"
             "\n"
             "Перевір чи коректно проведена заявка, поле «Статус SWE» повинно бути «Виконано».\n\n"
             "Якщо ви виконали рух ТО в УСД і локація ТО змінилася в УСД та SWE на коректну, але згідно"
             " з звітом обладнання залишилось у розбіжності, необхідно написати на пошту "
             f"\n👉 {capex}"
             ", вказуючи назву складу, код SWE ХО (номер обладнання) та контактний номер телефону в запиті.",
        photo=link_google_photo + "1zJhnJHRWXSIuMDjDVBBXWlv64uOjLYUB",

        parse_mode="HTML",
        reply_markup=errors_keyboard_ex
    )
    await callback.answer()


@errors_router.callback_query(BuyCallbackFactory.filter(F.item_name == "errors_few_dock"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Декілька документів на одне ТО?</b>\n"
             "\n"
             "<b>Вибило помилку вище?</b>\n\n"
             "Перевір усі документи по даному ТО, якщо є неактуальні, не проведені документи (заявки) – "
             "закрий зі статусом «Не выполнено».",
        photo=link_google_photo + "1TehvxjBfeP9Ro5L-EkOOKSMoaVvKdWjw",
        parse_mode="HTML",
        reply_markup=errors_keyboard_ex
    )
    await callback.answer()


@errors_router.callback_query(BuyCallbackFactory.filter(F.item_name == "errors_no_req"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        # текст станет caption для фото
        text=(
            "<b>✅ Не вдається провести заявку?</b>\n\n"

            "Якщо тех. стан «В ремонті» або «На списання» – пиши запит"
            f'👉 {coolers}\n\n'
            "Якщо ТО втрачене – надай фото шильда/QR та зовнішнього вигляду"
            f'👉 {coolers}\n\n'
            "Якщо не вдається провести заявку, оскільки ТО у втратах і немає можливості надати фото шильда, "
            "заявку необхідно заблокувати та звернутися до сектору продажів для створення нової — "
            "після фактичного надання фото шильда."
        ),
        photo=link_google_photo + "1JMIUWlyRo91EPcFyNM5_K0hHKkpgnVRB",
        parse_mode="HTML",
        reply_markup=errors_keyboard_ex
    )
    await callback.answer()


@errors_router.callback_query(BuyCallbackFactory.filter(F.item_name == "errors_field_req"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        # текст станет caption для фото
        text=(
            "<b>✅ Пусті поля в заявці?</b>\n\n"
            "Перевір чи є відкриті вкладки, як зображено на малюнку.\n"
            "Перезайди в робоче місце та провались в заявку знову.\n"
            "Якщо проблема не усунена напиши запит на "
            f"👉 {capex}"
            ", надаючи скріншот екрану"
        ),
        photo=link_google_photo + "1WUPLid2bC3iorxjsBLojSH42AZCW9_zc",
        parse_mode="HTML",
        reply_markup=errors_keyboard_ex
    )
    await callback.answer()


# errors_field_req


# errors_keyboard_st1_ex

@errors_router.callback_query(BuyCallbackFactory.filter(F.item_name == "errors_add_equip_s1"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        # текст станет caption для фото
        text="<b>✅ Додати обладнання в групове переміщення</b>?\n\n"
             "При проведенні переміщення між складами БСЦ створює «Планове переміщення»,"
             " після того як «Планове переміщення» буде завантажено до 1С Вам необхідно"
             " додати обладнання, для цього необхідно виконати дії прописані на схемі вище.",
        photo=link_google_photo + "11puKx73xuAVB8pa5Bf9sD3EoQVyc8cfA",
        parse_mode="HTML",
        reply_markup=errors_keyboard_st1_ex
    )
    await callback.answer()
