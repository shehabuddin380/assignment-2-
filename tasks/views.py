from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Event, Category, Participant
from .forms import EventForm, CategoryForm, ParticipantForm


def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'tasks/event_list.html', {'events': events})


@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Event created successfully.")
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'tasks/event_form.html', {'form': form})


@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully.")
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'tasks/event_form.html', {'form': form})


@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted.")
        return redirect('event_list')
    return render(request, 'tasks/event_confirm_delete.html', {'event': event})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'tasks/category_list.html', {'categories': categories})


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'tasks/category_form.html', {'form': form})


@login_required
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


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'tasks/category_confirm_delete.html', {'category': category})


def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'tasks/participant_list.html', {'participants': participants})


@login_required
def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'tasks/participant_form.html', {'form': form})


@login_required
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


@login_required
def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'tasks/participant_confirm_delete.html', {'participant': participant})


@login_required
def dashboard(request):
    total_events = Event.objects.count()
    total_participants = Participant.objects.count()
    upcoming_events = Event.objects.order_by('date')[:5]
    context = {
        'total_events': total_events,
        'total_participants': total_participants,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'tasks/dashboard.html', context)


def event_search(request):
    query = request.GET.get('q', '')
    events = Event.objects.filter(
        Q(name__icontains=query) | Q(location__icontains=query)
    ) if query else Event.objects.none()
    return render(request, 'tasks/event_search.html', {'events': events, 'query': query})


@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.user in event.rsvp_users.all():
        event.rsvp_users.remove(request.user)
        messages.info(request, "RSVP cancelled.")
    else:
        event.rsvp_users.add(request.user)
        messages.success(request, "RSVP confirmed.")
    return redirect('event_list')