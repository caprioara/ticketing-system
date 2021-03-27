from django import forms
from .models import Ticket
from django.forms import ClearableFileInput

class MyClearableFileInput(ClearableFileInput):
    initial_text = ''
    input_text = ''

class TicketForm(forms.ModelForm):

    slug = forms.ImageField(widget=MyClearableFileInput)

    class Meta:
        model = Ticket
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['slug'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['slug'].label_suffix = ''
        self.fields['slug'].label = ''
        self.fields['slug'].required = False

        self.fields['author'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['category'].widget.attrs.update(
            {'class': 'form-select'})

        self.fields['departament'].widget.attrs.update(
            {'class': 'form-select'})

        self.fields['content'].widget.attrs.update(
            {'class': 'form-control'})