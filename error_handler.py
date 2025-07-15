from fastapi.responses import JSONResponse
from fastapi import status, Request
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

async def custom_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, RequestValidationError) or isinstance(exc, ValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "error": "validation_error",
                "details": exc.errors() if hasattr(exc, "errors") else str(exc)
            }
        )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "internal_server_error",
            "details": str(exc)
        }
    )
