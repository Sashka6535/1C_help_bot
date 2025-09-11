from aiogram.fsm.context import FSMContext
from aiogram.types import InputFile, InputMediaPhoto, InputMediaDocument

async def edit_or_send_message(
    bot,
    chat_id,
    state: FSMContext,
    text: str = None,
    reply_markup=None,
    photo: str | InputFile = None,
    document: str | InputFile = None,
    parse_mode: str = None
):
    data = await state.get_data()
    first_message_id = data.get("first_message_id")

    # Если уже есть стартовое сообщение → редактируем
    if first_message_id:
        try:
            if photo:
                await bot.edit_message_media(
                    chat_id=chat_id,
                    message_id=first_message_id,
                    media=InputMediaPhoto(media=photo, caption=text, parse_mode = parse_mode),
                    reply_markup=reply_markup
                )
                return
            elif document:
                await bot.edit_message_media(
                    chat_id=chat_id,
                    message_id=first_message_id,
                    media=InputMediaDocument(media=document, caption=text, parse_mode = parse_mode),
                    reply_markup=reply_markup,
                    parse_mode = parse_mode
                )
                return
        except Exception as e:
            print(f"Ошибка при редактировании: {e}")

    # Если ещё нет стартового сообщения → отправляем новое (с фото или документом)
    if photo:
        sent = await bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=text,
            reply_markup=reply_markup
        )
    elif document:
        sent = await bot.send_document(
            chat_id=chat_id,
            document=document,
            caption=text,
            reply_markup=reply_markup
        )
    else:
        raise ValueError("Нужно передать либо photo, либо document!")

    # сохраняем ID стартового сообщения
    await state.update_data(first_message_id=sent.message_id)
