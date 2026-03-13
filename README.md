# Telegram Message Saver Bot

A Telegram bot that saves user messages to PostgreSQL.

## Stack

- **python-telegram-bot 21** — polling
- **SQLAlchemy 2 (async)** + asyncpg
- **PostgreSQL 16**
- **Docker Compose**

## Setup
```bash
cp .env.example .env
# paste your BOT_TOKEN into .env
docker compose up --build
```

## How it works

1. User sends any text message
2. Bot saves `user_id`, `username`, `text`, `created_at` to the `messages` table
3. Bot replies: **"Повідомлення збережено ✅"**

Table is created automatically on startup.