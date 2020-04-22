# forms.py
from django.forms import ModelForm
from .models import Pollmd


class CreatePollForm(ModelForm):
    class Meta:
        model = Pollmd
        fields = ['question', 'option_one', 'option_two', 'option_three']
