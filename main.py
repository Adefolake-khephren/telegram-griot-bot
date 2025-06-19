from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8149275598:AAE5rDDwW42Mc_fEs107VRHvoV_ohhZxYkk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👋🏾 Bienvenue âmes éveillées. Je suis ADEFOLAKÉ Z KHEPHREN. "
        "Ce bot est un espace de parole libre, poétique et décoloniale. ✊🏾\n"
        "Tape /poeme, /citation ou /résistance pour commencer."
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot actif ! Laisse cet onglet ouvert pour qu’il fonctionne.")
    app.run_polling()
