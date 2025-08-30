from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = "tasks/event_list.html"
    context_object_name = "events"

class EventDetailView(DetailView):
    model = Event
    template_name = "tasks/event_detail.html"
    context_object_name = "event"

class EventCreateView(CreateView):
    model = Event
    fields = ["title", "description", "date", "category", "image"]
    template_name = "tasks/event_form.html"
    success_url = reverse_lazy("event-list")

class EventUpdateView(UpdateView):
    model = Event
    fields = ["title", "description", "date", "category", "image"]
    template_name = "tasks/event_form.html"
    success_url = reverse_lazy("event-list")

class EventDeleteView(DeleteView):
    model = Event
    template_name = "tasks/event_confirm_delete.html"
    success_url = reverse_lazy("event-list")
