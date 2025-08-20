from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    raw_text = models.TextField()
    task = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=50, blank=True)
    reminder_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task or self.raw_text[:30]
    
class Reminder(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="reminders")
    run_at = models.DateTimeField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder<{self.note_id} @ {self.run_at}>"
    
    