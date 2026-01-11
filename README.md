# Webhook Ingestion Service

A FastAPI-based service that securely receives webhooks, validates a shared secret,
stores payloads in a database, and ensures idempotent processing.

## Features
- POST /webhook endpoint
- Header-based authentication (X-Signature)
- PostgreSQL database
- Idempotency via unique event_id
- Clean JSON responses

## Tech Stack
FastAPI, SQLAlchemy, PostgreSQL, Pydantic

## Running Locally

### Prerequisites
- Python 3.11 installed
- `pip` for package management
- Clone the repository to your local machine

### Steps to Run Locally

1. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add the following:
   ```env
   DATABASE_URL=postgresql:///./test.db
   SECRET_KEY=your_secret_key_here
   ```

4. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:8000`.

6. **Test the webhook endpoint:**
   Use tools like `curl` or Postman to send POST requests to `/webhook`.

## Example Request

```bash
curl -X POST http://127.0.0.1:8000/webhook \
  -H "Content-Type: application/json" \
  -H "X-Signature: supersecret123" \
  -d '{"event_id": "abc123", "action": "user_created"}'
```

## Example Webhook Payload
```json
{
  "event_id": "12345",
  "event_type": "example_event",
  "data": {
    "key": "value"
  }
}
```
