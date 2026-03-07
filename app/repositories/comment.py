from sqlalchemy import select
from app.models.comments import Comment
from app.repositories.base import BaseRepository


class CommentRepository(BaseRepository):
    async def create(
        self,
        *,
        org_id,
        ticket_id,
        author_id,
        body: str,
        is_internal: bool = False,
    ) -> Comment:
        comment = Comment(
            org_id=org_id,
            ticket_id=ticket_id,
            author_id=author_id,
            body=body,
            is_internal=is_internal,
        )
        self.session.add(comment)
        await self.session.flush()
        await self.session.refresh(comment)
        return comment
