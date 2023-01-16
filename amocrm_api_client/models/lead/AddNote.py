from typing import Literal

from pydantic import BaseModel

__all__ = [
    "AddNote",
    "NoteTypes"
]


class ServiceMessageParams(BaseModel):
    service: str | None
    text: str


NoteTypes = Literal['service_message', 'common',
                    'call_in', 'call_out', 'message_cashier', 'geolocation', 'sms_in', 'sms_out', 'extended_service_message']



class AddNote(BaseModel):
    entity_id: int
    note_type: NoteTypes
    params: ServiceMessageParams
