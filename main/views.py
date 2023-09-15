from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from .import forms
from .models import Aircraft
from .database import Client
import urllib.parse
import os


client = Client()

def home(request):
    return render(request, 'main/home.html')

@login_required(login_url="/login")
def atc(request):
    if request.method == "POST":
        form = forms.AirportForm(request.POST)
        icao = None
        if form.is_valid():
            icao = form.cleaned_data["airport"]
        return redirect(f"atc/{icao}")
    else:
        airport = forms.AirportForm()
        return render(request, 'main/atc.html', context={"form" : airport})

@login_required(login_url="/login")
def airport(request, icao : str):
    if request.method == "GET":
        chart_dirs = client.get_Charts(icao)
        callsign = request.GET.get("callsign")
        runway = request.GET.get("runway")
        if not client.runway_valid(icao, runway):
            runway = client.get_default_runway(icao)
            return redirect(f"/atc/{icao}?runway={runway}&callsign={callsign}")
        airways = []
        for chart in chart_dirs.airway:
            if str.find(os.path.basename(chart), runway) >= 0:
                airways.append(chart)
        aircrafts = Aircraft.objects.all()
        print(aircrafts)
        return render(request, 'main/airport.html', context={"ICAO" : icao, "Ground_Charts" : chart_dirs.ground, "Airway_Charts" : airways, "Callsign" : callsign, "aircrafts" : aircrafts})
    else:
        return HttpResponseBadRequest("Post request was made, which is unsupported")