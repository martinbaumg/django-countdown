from .models import Event
from django import forms
from . import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _


class EventForm(ModelForm):
        class Meta:
            model = Event
            fields = (
                'name',
                'date',
                'description',
                )
            labels = {"name":"Nom :", "nom":"Nom :", "description":"Description :"}
