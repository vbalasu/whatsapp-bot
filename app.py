from chalice import Chalice
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

app = Chalice(app_name="whatsapp-bot")

# Twilio Credentials - Set these as environment variables
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.environ.get("TWILIO_WHATSAPP_NUMBER")

@app.route("/send-message", methods=["POST"], cors=True)
def send_message():
    request = app.current_request.json_body
    to_number = request.get("to")
    message = request.get("message")

    if not to_number or not message:
        return {"error": "Missing 'to' or 'message' field"}

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    msg = client.messages.create(
        body=message,
        from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
        to=f"whatsapp:{to_number}"
    )

    return {"message_sid": msg.sid, "status": "Message sent"}