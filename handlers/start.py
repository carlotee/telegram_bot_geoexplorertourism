from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! 👋 Bienvenido a GeoExplorerTourism.\n\n"
        "Descubre lugares turísticos y encuentra tu próximo destino.\n\n"
        "Estos son los comandos disponibles:\n"
        "/lugares - Explorar lugares turísticos\n"
        "/hola - Comprobar que el bot funciona\n"
        "/ayuda - Mostrar los comandos disponibles"
    )


async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! 😎 El bot está funcionando correctamente."
    )


async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Comandos de GeoExplorerTourism\n\n"
        "/start - Iniciar el bot\n"
        "/lugares - Explorar lugares turísticos\n"
        "/hola - Enviar un saludo\n"
        "/ayuda - Consultar los comandos disponibles"
    )
