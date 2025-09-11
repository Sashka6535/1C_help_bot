from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Handlers.link_photo import logo_photo, link_google_photo, capex, coolers
from Handlers.delete_mes import edit_or_send_message
from Keyboards.callback_datas import BuyCallbackFactory
from Keyboards.keyb_inconsistencies.keyb_location import inconsis_reloc, inconsis_reloc_ex
from Keyboards.keyb_inconsistencies.keyb_not_osd import inconsis_not_osd_ex, inconsis_not_osd

location_router = Router()

@location_router.callback_query(BuyCallbackFactory.filter(F.item_name == "no_lock"))
async def handle_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>Відрізняється локація ❌</b>",
        photo=logo_photo,
        parse_mode="HTML",
        reply_markup=inconsis_reloc
    )
    await callback.answer()


@location_router.callback_query(BuyCallbackFactory.filter(F.item_name == "reloc_req_tehcond"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Не проводиться заявка через тех. стан ТО?</b>\n"
             "\n"
             "Якщо тех. стан «В ремонті» або «На списання» – пиши запит"
             f'👉 {coolers}\n'
             "Якщо ТО втрачене – надай фото шильда/QR та зовнішнього вигляду "
             f'👉 {coolers}',
        photo=link_google_photo + "1ialKxfoH6_jLoUGALuW0M3Eq-dKpwDuf",
        parse_mode="HTML",
        reply_markup=inconsis_reloc_ex
    )
    await callback.answer()

@location_router.callback_query(BuyCallbackFactory.filter(F.item_name == "reloc_req_done"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        text="<b>✅ Зависла виконана заявка в системі?</b>\n"
             "\n"
             "Перевір чи коректно проведена заявка, поле «Статус SWE» повинно бути «Виконано».\n\n"
             "Якщо ви виконали рух ТО в УСД і локація ТО змінилася в УСД та SWE на коректну, але згідно"
             " з звітом обладнання залишилось у розбіжності, необхідно написати на пошту "
             f"\n👉 {capex}"
             ", вказуючи назву складу, код SWE ХО (номер обладнання) та контактний номер телефону в запиті.",
        photo=link_google_photo + "17I4BX60k3IYEdqeD4Qj9j8y_pdQWaqKR",
        parse_mode="HTML",
        reply_markup=inconsis_reloc_ex
    )
    await callback.answer()


#@location_router.callback_query(BuyCallbackFactory.filter(F.item_name == "reloc_osd"))
#async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    #    await edit_or_send_message(
    #    bot=callback.bot,
    #    chat_id=callback.message.chat.id,
    #    state=state,
    #    # текст станет caption для фото
    #    text=(
    #        "✅ Потрібно провести ручну заявку?\n\n"
    #        "Перевір коректність тех. стану, він повинен бути «нове» або «робоче».\n"
    #        "Перевір коректність необхідної точки, можливо вона стала неактивною і була створена аналогічна точка, "
    #        "але з іншим зовнішнім кодом.\n"
    #        "Якщо зависла проведена ручна заявка – пиши БСЦ на пошту "
    #        '👉 <a href="mailto:BSC.Capex.UA@abinbevefes.com.ua">BSC.Capex.UA@abinbevefes.com.ua</a> '
    #        "для перевірки коректності ТТ в системі SWE."
    #        ),
    #    photo="https://drive.google.com/uc?export=view&id=1AnSswVSu2oc97Nc1904fmJoQ2lohSX9P",
    #    parse_mode="HTML",
    #    reply_markup=inconsis_reloc
    #)
    #await callback.answer()

@location_router.callback_query(BuyCallbackFactory.filter(F.item_name == "reloc_req_inv"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        # текст станет caption для фото
        text=(
            "<b>✅ Провели заявки в період інвентаризації?</b>\n\n"
            "У період складської інвентаризації проведення переміщень ТО в системі ЗАБОРОНЕНО 🚫\n\n"
            "Якщо переміщення проводилися, вивантаж дані з 1С після закриття хвилі за всі дати інвентаризації "
            "і перевір, чи усунулися розбіжності в звіті «Отчёт по оборудованию».\n\n"
            "Якщо розбіжності залишилися – пиши запит"
            f'👉 {capex}'
            "надаючи скріншот виконаної заявки для перевірки прогрузки рухів у системі SWE."
        ),
        photo=link_google_photo + "1gy38EnLMlLgTqKeWbKcezkBueN93AzhH",
        parse_mode="HTML",
        reply_markup=inconsis_reloc_ex
    )
    await callback.answer()

@location_router.callback_query(BuyCallbackFactory.filter(F.item_name == "reloc_rename_tt"))
async def handle_back_not_swe(callback: CallbackQuery, state: FSMContext):
    await edit_or_send_message(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        state=state,
        # текст станет caption для фото
        text=(
                "<b>✅ Виникла розбіжність через перейменування ТТ?</b>\n\n"
                "Створюємо вручну заявку на переміщення з ТТ у ТТ (стовпець «Место хранения УСД»)"
                " у ТТ (стовпець «Место хранения SWE») в 1С та вирівнюємо локацію ТО."
            ),
        photo=link_google_photo + "1h5gjlkiMDeOkZo4kBUAAf-2y8dCc2ev6",
        parse_mode="HTML",
        reply_markup=inconsis_reloc_ex
    )
    await callback.answer()