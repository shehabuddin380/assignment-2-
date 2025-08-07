from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Participant, Category
from .forms import EventForm, ParticipantForm, CategoryForm
from django.db.models import Count, Q
from datetime import date
from django.contrib import messages



def event_list(request):
    search = request.GET.get('q', '')
    events = Event.objects.select_related('category').prefetch_related('participants')
    if search:
        events = events.filter(Q(name__icontains=search) | Q(location__icontains=search))
    return render(request, 'event_list.html', {'events': events, 'search': search})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'tasks/event_form.html', {'form': form})

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'tasks/event_form.html', {'form': form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event_list')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'tasks/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'tasks/category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'tasks/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')


# Participant Views
def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'tasks/participant_list.html', {'participants': participants})


# Dashboard
def dashboard(request):
    today = date.today()
    events = Event.objects.all()
    total_events = events.count()
    total_participants = Participant.objects.count()
    upcoming_events = events.filter(date__gt=today).count()
    past_events = events.filter(date__lt=today).count()
    todays_events = events.filter(date=today)
    return render(request, 'tasks/dashboard.html', {
        'total_events': total_events,
        'total_participants': total_participants,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'todays_events': todays_events
    })

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'tasks/participant_list.html', {'participants': participants})

def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'tasks/participant_form.html', {'form': form})

def participant_update(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'tasks/participant_form.html', {'form': form})

def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    participant.delete()
    return redirect('participant_list')

def event_search(request):
    query = request.GET.get('q', '')
    results = Event.objects.filter(
        Q(name__icontains=query) | Q(location__icontains=query)
    )
    return render(request, 'tasks/event_search.html', {'events': results, 'query': query})

def home(request):
    return render(request, 'tasks/home.html')

@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.user in event.rsvp_users.all():
        messages.warning(request, "You have already RSVP'd to this event.")
    else:
        event.rsvp_users.add(request.user)
        messages.success(request, "RSVP successful!")
    return redirect('event_list')
