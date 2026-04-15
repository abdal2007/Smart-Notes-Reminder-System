
# Smart Notes & Reminder System  

## 🎥 Demo Videos


https://github.com/user-attachments/assets/9035237b-f97e-41e0-bc75-62babcbc970b




##  Overview  
A Django based Smart notes **AI powered reminder app** which converts language text to structured reminder.

- User signup/login to manage notes and reminders 
- AI (OpenAI GPT) extract **task, category and reminder time** 
-  On reminder due Celery background worker  **send Email notification to the user**  
- Only logedin user can view their notes and reminders

---

## Features  
-  **User Authentication** (Signup/Login/Logout with sessions)  
-  **AI-Powered Note Parsing** (task, category, datetime)  
-  **Email Reminders via Celery + Redis**  
-  **Bootstrap Frontend Templates** (Notes, Reminders, Auth pages)  
-  **REST APIs (DRF)** for integration  

---

## Tech Stack  
- **Backend:** Django + DRF  
- **Auth:** Django session-based login  
- **AI:** OpenAI GPT (via `.env` API key)  
- **Scheduler:** Celery + Redis  
- **Database:** SQLite (dev) 
- **Frontend:** Django Templates (Bootstrap 5 + optional voice input)  
- **Email:** Gmail SMTP 

---

## Installation  

### Clone Project  
```bash
git clone [<repo_url>](https://github.com/abdal2007/Smart-Notes-Reminder-System.git)
cd smartnotes
```
### Virtual Environment & Dependencies
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
### Setup .env File
```bash
OPENAI_API_KEY=sk-xxxxxx
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=yourgmail@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
DEFAULT_FROM_EMAIL=yourgmail@gmail.com
```
### Migrate Database
```bash
python manage.py makemigrations
python manage.py migrate
```
### Run Django Server
```bash
python manage.py runserver
```
### Run Celery
```bash
celery -A smartnotes worker -l info --pool=solo
celery -A smartnotes beat -l info
```
## Usage Flow
- Signup → account create
- Login → session start
- Notes page → reminder text ("Remind me to call bank tomorrow at 10 AM")
- AI parse the text and save it in the DB
- At due time → Celery sent email to user Gmail
  


