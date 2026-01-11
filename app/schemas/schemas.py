from pydantic import BaseModel


class WebhookEventPayload(BaseModel):
    event_id: str
    event_type: str
    data: dict

class WebhookResponse(BaseModel):
    status: str
    message: str
