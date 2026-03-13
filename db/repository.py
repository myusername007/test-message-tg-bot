from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Message


async def save_message(
    session: AsyncSession,
    user_id: int,
    username: str | None,
    text: str,
) -> Message:
    msg = Message(user_id=user_id, username=username, text=text)
    session.add(msg)
    await session.commit()
    return msg