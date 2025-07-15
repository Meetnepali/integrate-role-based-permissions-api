from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from feedback import router as feedback_router
from error_handler import custom_exception_handler
from fastapi.exception_handlers import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register router
app.include_router(feedback_router)

# Register custom error handler
app.add_exception_handler(Exception, custom_exception_handler)
app.add_exception_handler(RequestValidationError, custom_exception_handler)

@app.get("/")
def root():
    return {"message": "Feedback API running"}
