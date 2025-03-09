#ENDPOINT=http://127.0.0.1:8000/send-message
ENDPOINT=https://pyf28n8elf.execute-api.us-east-1.amazonaws.com/api/send-message

curl -X POST $ENDPOINT \
     -H "Content-Type: application/json" \
     -d '{"to": "+17324232445", "message": "Hello from WhatsApp bot!"}'
