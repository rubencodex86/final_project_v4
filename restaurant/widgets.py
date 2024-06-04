from django import forms
from datetime import time


class CustomTimeInput(forms.Select):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = self.get_time_choices()

    def get_time_choices(self):
        choices = []
        for hour in range(9, 23):
            choices.append((time(hour, 0).strftime("%H:%M"), time(hour, 0).strftime("%I:%M %p")))
            choices.append((time(hour, 30).strftime("%H:%M"), time(hour, 30).strftime("%I:%M %p")))
        return choices
