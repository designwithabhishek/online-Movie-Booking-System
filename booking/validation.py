from django.forms import forms
from datetime import date,time
from django.utils import timezone
def validate_date_show(value):
    current_date=date.today()
    if value < current_date:
        raise forms.ValidationError("Invalid date")