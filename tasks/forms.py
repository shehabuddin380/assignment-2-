from django import forms
from .models import Event, Category, Participant

INPUT_CLASS = "w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 4}),
            'date': forms.DateInput(attrs={'class': INPUT_CLASS, 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': INPUT_CLASS, 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'category': forms.Select(attrs={'class': INPUT_CLASS}),
            'image': forms.ClearableFileInput(attrs={'class': INPUT_CLASS}),
            'rsvp_users': forms.SelectMultiple(attrs={'class': INPUT_CLASS}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 3}),
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'email': forms.EmailInput(attrs={'class': INPUT_CLASS}),
            'events': forms.SelectMultiple(attrs={'class': INPUT_CLASS}),
        }