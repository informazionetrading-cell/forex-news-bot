import requests
import xml.etree.ElementTree as ET
import os
from datetime import datetime

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
# Feed RSS di Forex Factory per la settimana corrente
FF_FEED = "https://www.forexfactory.com/ff_calendar_thisweek.xml"

def main():
    try:
        response = requests.get(FF_FEED, headers={'User-Agent': 'Mozilla/5.0'})
        root = ET.fromstring(response.content)
        
        # Oggi in formato Forex Factory (es: 02-27-2026)
        today = datetime.now().strftime("%m-%d-%Y")
        news_found = False

        for item in root.findall('event'):
            date = item.find('date').text
            impact = item.find('impact').text
            
            # Filtriamo: Solo news di OGGI e solo ad ALTO IMPATTO (High)
            if date == today and impact == 'High':
                title = item.find('title').text
                country = item.find('country').text
                time = item.find('time').text
                
                send_to_discord(title, country, time)
                news_found = True
        
        if not news_found:
            print("Nessuna news ad alto impatto trovata per oggi.")

    except Exception as e:
        print(f"Errore: {e}")

def send_to_discord(title, country, time):
    color = 15158332  # Rosso per High Impact
    payload = {
        "embeds": [{
            "title": f"🚨 NEWS ALTO IMPATTO: {country}",
            "description": f"**Evento:** {title}\n**Ora:** {time} (EST)",
            "color": color,
            "footer": {"text": "Forex Factory Calendar"}
        }]
    }
    requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    main()
