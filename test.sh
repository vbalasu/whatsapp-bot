curl -X POST http://127.0.0.1:8000/send-message \
     -H "Content-Type: application/json" \
     -d '{"to": "+17324232445", "message": "Hello from WhatsApp bot!"}'
