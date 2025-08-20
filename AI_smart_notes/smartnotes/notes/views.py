from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView, ListView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note, Reminder
from .serializers import NoteSerializer, ReminderSerializer
from .services import parse_note_ai
from django.contrib.auth.models import User

# Create your views here.
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")

class UserLoginView(LoginView):
    template_name = "login.html"

class HomeView(TemplateView):
    template_name = "home.html"

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = "notes.html"
    context_object_name = "notes"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        text = request.POST.get("text")
        if text:
            parsed = parse_note_ai(text)
            note = Note.objects.create(
                user=request.user,
                raw_text=text,
                task=parsed["task"],
                category=parsed["category"],
                reminder_time=parsed["when"]
            )
            if parsed["when"]:
                Reminder.objects.create(note=note, run_at=parsed["when"])
        return self.get(request, *args, **kwargs)


class ReminderListView(LoginRequiredMixin, ListView):
    model = Reminder
    template_name = "reminders.html"
    context_object_name = "reminders"

    def get_queryset(self):
        return Reminder.objects.filter(note__user=self.request.user).order_by("run_at")






