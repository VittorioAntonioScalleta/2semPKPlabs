from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
START, INFO, HELP = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Привет! Я бот-конечный автомат. Вы можете использовать команды:\n"
        "/info - Получить информацию\n"
        "/help - Получить помощь\n"
        "/start - Начать сначала"
    )
    return START

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Это информация о работе бота. Вы можете вернуться к началу с помощью команды /start."
    )
    return INFO

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Это справка. Используйте команду /start для возврата в начальное состояние."
    )
    return HELP

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Бот завершил работу. До свидания!")
    return ConversationHandler.END

def main():
    application = Application.builder().token("*******************").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [
                CommandHandler("info", info),
                CommandHandler("help", help_command),
            ],
            INFO: [
                CommandHandler("start", start),
                CommandHandler("help", help_command),
            ],
            HELP: [
                CommandHandler("start", start),
                CommandHandler("info", info),
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
