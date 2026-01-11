from fastapi import APIRouter, Depends
from json import JSONDecodeError
from sqlalchemy.orm import Session
from app.db.database import SessionLocal, get_db
from app.model.models import WebhookEvent
from app.schemas.schemas import WebhookResponse, WebhookEventPayload
from app.utils.security import verify_signature
router = APIRouter()

@router.post("/webhook", response_model=WebhookResponse)
async def receive_webhook(
    payload: WebhookEventPayload,
    db: Session = Depends(get_db),
    _: str = Depends(verify_signature),
):
    # payload is already validated JSON
    event_id = payload.event_id

    existing = db.query(WebhookEvent).filter_by(event_id=event_id).first()
    if existing:
        return {"status": "ignored", "message": "Duplicate event"}

    event = WebhookEvent(
        event_id=payload.event_id,
        payload=payload.dict()
    )

    db.add(event)
    db.commit()

    return {"status": "success", "message": "Event stored"}
