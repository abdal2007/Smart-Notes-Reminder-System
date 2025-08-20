from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from .models import Reminder

@shared_task
def send_due_reminders():
    now = timezone.now()
    due = Reminder.objects.filter(sent=False, run_at__lte=now)
    for r in due:
        send_mail(
            subject=f"Reminder: {r.note.task}",
            message=f"Hi! It's time: {r.note.raw_text}",
            from_email=None,
            recipient_list=[r.note.user.email],  
        )
        r.sent = True
        r.save()
    return f"Sent {due.count()} reminders"
