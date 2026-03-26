import os
import time
from telegram import Update
from telegram.error import BadRequest
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

from equipe_agentes.agente_orquestrador import perguntar_agente

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem_usuario = update.message.text
    
    try:
        mensagem_status = await update.message.reply_text("⏳ Consultando informações...")
    
        resposta_final = perguntar_agente(mensagem_usuario) 
        
        if resposta_final:
            await mensagem_status.edit_text(resposta_final)
            
        else:
            await mensagem_status.edit_text("Não consegui formular uma resposta.")
            
    except Exception as e:
        await update.message.reply_text('❌ Erro interno ao processar sua solicitação.')


def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, responder))
    app.run_polling()