from django import forms
from . import database

cl = database.Client()

options = []

for code in cl.get_airports():
    options.append((f"{code}", code))

class AirportForm(forms.Form):
    airport = forms.ChoiceField(choices=options, required=True)