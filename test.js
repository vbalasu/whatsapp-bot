// Works in nodejs and the browser
fetch('https://whatsapp.cloudmatica.com/send-message', {method: 'POST', body: '{"to": "+17324232445", "message": "Hello from WhatsApp bot!"}', headers: {'Content-Type': 'application/json'}}).then(response => response.json())
