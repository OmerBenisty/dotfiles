curl --request POST \
--url https://api.sendgrid.com/v3/mail/send \
--header 'Authorization: Bearer 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' \
--header 'Content-Type: application/json' \
--data '{"personalizations":[{"to":[{"email":"omerb@inmanage.co.il","name":"John Doe"}],"subject":"Hello, World!"}],"content": [{"type": "text/plain", "value": "Heya!"}],"from":{"email":"sam.smith@example.com","name":"Sam Smith"},"reply_to":{"email":"sam.smith@example.com","name":"Sam Smith"}}'
