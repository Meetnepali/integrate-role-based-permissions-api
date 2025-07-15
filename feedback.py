from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel, EmailStr, ValidationError, validator
from typing import Optional

router = APIRouter(prefix="/feedback", tags=["feedback"])

class Feedback(BaseModel):
    email: EmailStr
    message: str
    rating: Optional[int] = None

    @validator("message")
    def message_min_length(cls, v):
        if not v or len(v.strip()) < 10:
            raise ValueError("Message must be at least 10 characters long.")
        return v

    @validator("rating")
    def rating_valid(cls, v):
        if v is not None and (v < 1 or v > 5):
            raise ValueError("Rating must be between 1 and 5.")
        return v

def send_email_simulation(email: str):
    print(f"Simulated email sent: Thank you, {email}, for your feedback!")

@router.post("/", status_code=201)
async def submit_feedback(feedback: Feedback, background_tasks: BackgroundTasks):
    # Simulate an asynchronous email sending confirmation
    background_tasks.add_task(send_email_simulation, feedback.email)
    return {"detail": "Feedback received"}
