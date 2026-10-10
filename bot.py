
import os

from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

from handlers.start import start, hola, ayuda

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError(
        "No se encontró TELEGRAM_TOKEN. Revisa tu archivo .env."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hola", hola))
app.add_handler(CommandHandler("ayuda", ayuda))

print("Bot de GeoExplorerTourism iniciado correctamente.")
app.run_polling()
