import requests
import os

# URL del Webhook che hai salvato nei "Secrets"
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def main():
    # Per ora facciamo un test semplice per vedere se Discord riceve
    payload = {
        "embeds": [{
            "title": "Forex Factory News Bot",
            "description": "Il bot è attivo! Sta monitorando le news ad alto impatto per te. 🚀",
            "color": 15158332 # Rosso
        }]
    }
    
    if WEBHOOK_URL:
        requests.post(WEBHOOK_URL, json=payload)
        print("Messaggio inviato a Discord!")
    else:
        print("Errore: Webhook non trovato nei Secrets.")

if __name__ == "__main__":
    main()
