# Guidance for Task

This project is a containerized FastAPI web service that exposes a feedback module. Users can submit feedback containing their email, message, and an optional rating. The system must validate the input and asynchronously simulate an email notification via a background task (console output).

Requirements are:
- Validate input for required fields (valid email, minimum message length, optional rating between 1-5)
- Organize the feedback logic in a dedicated APIRouter
- Process feedback submissions with a simulated background task
- Respond to all errors using a structured JSON format, using a global custom exception handler
- Containerize the app with a Dockerfile and manage dependencies using a Python virtual environment
- Provide install and run scripts for developer convenience

## Verifying Your Solution

After completing your implementation and launching the service, verify you can:
- Submit valid feedback and receive a success message
- See confirmation of simulated email in standard output
- Submit invalid data and receive structured JSON errors with the appropriate HTTP status codes

Only the files relevant to the feedback submission, error handling, router integration, and containerization are part of this task. No database, authentication, monitoring, or real outgoing emails are expected.
