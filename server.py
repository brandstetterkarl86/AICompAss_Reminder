from flask import Flask, Response
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/generate_ics")
def generate_ics():
    # Berechnung: Immer "heute +14 Tage"
    today = datetime.utcnow()
    event_date = today + timedelta(days=14)

    # Dynamische ICS-Datei
    ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//AICompAss Dynamic Reminder//EN
BEGIN:VEVENT
UID:AICompAss-Dynamic-Reminder
DTSTAMP:{today.strftime('%Y%m%dT%H%M%SZ')}
DTSTART:{event_date.strftime('%Y%m%dT090000Z')}
DTEND:{event_date.strftime('%Y%m%dT093000Z')}
SUMMARY:🔔 AICompAss – Erinnerung für Folgeerhebung!
DESCRIPTION:Bitte denken Sie an Ihre nächste AICompAss-Teilnahme: https://limesurvey.fh-campuswien.ac.at/index.php/642898?lang=de
BEGIN:VALARM
TRIGGER:-PT15M
ACTION:DISPLAY
DESCRIPTION:Erinnerung: Ihre AICompAss-Umfrage steht bald an!
END:VALARM
END:VEVENT
END:VCALENDAR"""

    # ICS-Datei zum Download bereitstellen
    return Response(ics_content, mimetype="text/calendar",
                    headers={"Content-Disposition": "attachment; filename=AICompAss_Reminder.ics"})

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("Port", 5000)))
