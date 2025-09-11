from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Handlers.link_photo import logo_photo, link_google_photo, capex
from Handlers.delete_mes import edit_or_send_message
from Keyboards.callback_datas import BuyCallbackFactory
from Keyboards.keyb_inconsistencies.keyb_not_osd import inconsis_not_osd_ex, inconsis_not_osd

not_osd_router = Router()

@not_osd_router.callback_query(BuyCallbackFactory.filter(F.item_name == "no_osd"))
async def handle_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>Немає В ОСД ⭕️</b>",
        photo=logo_photo,
        parse_mode="HTML",
        reply_markup=inconsis_not_osd
    )
    await callback.answer()


@not_osd_router.callback_query(BuyCallbackFactory.filter(F.item_name == "osd_delswe"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Списали не те обладнання?</b>\n"
             "\n"
             "РОЗПРОВОДИМО списання ТО.\n"
             "У нижній частині, при натисканні на ТО, відображаються документи, "
             "які були раніше по ньому сформовані.\n"
             "Знаходимо документ списання, відкриваємо його подвійним натисканням правою кнопкою миші "
             "та натискаємо «Розпровести», закриваємо документ.\n"
             "‼️ВАЖЛИВО не натискати «Провести и закрить»‼️",
        photo=link_google_photo + "1USgIBHx2JgvYANneA6YzD7ksbhGn1AnN",
        parse_mode="HTML",
        reply_markup=inconsis_not_osd_ex
    )
    await callback.answer()


@not_osd_router.callback_query(BuyCallbackFactory.filter(F.item_name == "osd_noknow_to"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ З'явилось в 1С не твоє обладнання?</b>\n"
             "\n"
             "Якщо по ТО відобразилися пусті поля «Последнее перемещение» та «Документ-регистратор перемещения» "
             "і ТО не належить складу, пишемо запит на "
             f'👉 {capex} '
             "для виконання зміни відповідальності в SWE на коректний склад та подальшого формування АПП "
             "на вкладці «Ответственность».",
        photo=link_google_photo + "1pp2dJS4yEf3WcoP5ONlp37y7lufw5cCe",
        parse_mode="HTML",
        reply_markup=inconsis_not_osd_ex
    )
    await callback.answer()


@not_osd_router.callback_query(BuyCallbackFactory.filter(F.item_name == "osd_to_ka"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        # текст станет caption для фото
        text=(
            "<b>✅ З'явилось ТО з мережі КА?</b>\n\n"
            "<b>Відобразилося ТО, раніше встановлене в мережі КА?</b>\n\n"
            "Перевір заявку на демонтаж: якщо заявка є, проведи і розбіжність зникне.\n"
            "Якщо заявки немає, пиши на"
            f'👉 {capex}.'
        ),
        photo=logo_photo,
        parse_mode="HTML",
        reply_markup=inconsis_not_osd_ex
    )
    await callback.answer()

@not_osd_router.callback_query(BuyCallbackFactory.filter(F.item_name == "osd_otgruz"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        # текст станет caption для фото
        text=(
            "<b>✅ Висить розбіжність зі статусом «Отгружено»?</b>\n\n"
            "<b>Зависла заявка в розбіжності «Нет в УСД»?</b>\n\n"
            "Дивись статус ⚠️ – якщо «Отгружено», значить друкувалися документи.\n"
            "Закрий заявку «Выполнено/Не виполнено» і розбіжність зникне."
        ),
        photo=link_google_photo + "14VlhZ5htep0P5iqCxWaw6kw2vN9L1s3z",
        parse_mode="HTML",
        reply_markup=inconsis_not_osd_ex
    )
    await callback.answer()