from telegram import Update
from telegram.ext import ContextTypes

from db.repository import save_message
from db.session import AsyncSessionLocal


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привіт! Надішли мені будь-яке повідомлення."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    text = update.message.text

    async with AsyncSessionLocal() as session:
        await save_message(
            session,
            user_id=user.id,
            username=user.username,
            text=text,
        )

    await update.message.reply_text("Повідомлення збережено ✅")
