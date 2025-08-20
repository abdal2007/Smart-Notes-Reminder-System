from openai import OpenAI
from django.conf import settings
import dateparser
import json
from datetime import datetime, date, time

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def parse_note_ai(text):
    prompt = f"""
    Extract task, datetime, category from this reminder text:
    "{text}"

    Return JSON strictly like this:
    {{
      "task": "...",
      "datetime": "YYYY-MM-DD HH:MM:SS" or null,
      "category": "..."
    }}

    Rules:
    - If only time is mentioned (e.g., "5pm"), assume today ({datetime.now().date()}) in current year {datetime.now().year}.
    - If only day/month mentioned, assume current year {datetime.now().year}.
    - Categories: shopping, work, personal, or General if unclear.
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw = res.choices[0].message.content
    print("RAW AI RESPONSE:", raw)
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("```")[1]  # json part nikala
        cleaned = cleaned.replace("json", "", 1).strip()


    try:
        data = json.loads(cleaned)
    except Exception as e:
        print("JSON ERROR:", e)
        data = {"task": text[:50], "datetime": None, "category": "General"}

    dt = None
    if data.get("datetime"):
        dt = dateparser.parse(
        data["datetime"],
        settings={'TIMEZONE': 'Asia/Karachi', 'RETURN_AS_TIMEZONE_AWARE': True}
        )

    return {
    "task": data.get("task", text[:50]),
    "when": dt,
    "category": data.get("category", "General")
    }

