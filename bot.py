import os
from telegram import Update
from telegram.ext import Application, CommandHandler

# Ottieni il token dalle variabili d’ambiente
TOKEN = os.getenv("7602723607:AAEq7M9-7thz8-J7QOebcRCmZ6Ub05VcIrM")

async def start(update: Update, context):
    await update.message.reply_text("Ciao! Sono attivo su Railway.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot in esecuzione su Railway...")
    app.run_polling()

if __name__ == "__main__":
    main()
