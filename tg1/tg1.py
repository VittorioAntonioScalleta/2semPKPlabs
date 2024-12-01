from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

async def nachat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Эта", callback_data='1')],
        [InlineKeyboardButton("Вот эта", callback_data='2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выбери кнопку:', reply_markup=reply_markup)

async def knopka(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == '1':
        await query.edit_message_text(text="Неправильно")
    elif query.data == '2':
        await query.edit_message_text(text="Правильно")

def main():
    application = ApplicationBuilder().token("***************").build()
    application.add_handler(CommandHandler('nachat', nachat))
    application.add_handler(CallbackQueryHandler(knopka))
    application.run_polling()

if __name__ == '__main__':
    main()
