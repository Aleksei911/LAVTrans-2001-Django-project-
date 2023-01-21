from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete_to', 'worker']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            'complete_to': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Выполнить до (YYYY-MM-DD hh:mm:ss)'
            }),
        }
