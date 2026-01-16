from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .orbital_engine import SatelliteTracker
from .models import SatelliteLog
import json

TRACKER = SatelliteTracker()

def index(request):
    return render(request, 'index.html')

def get_satellites(request):
    return JsonResponse({'assets': TRACKER.get_current_positions()})

def get_trajectory(request):
    name = request.GET.get('name')
    return JsonResponse({'path': TRACKER.get_trajectory(name)})

def get_predictions(request):
    country = request.GET.get('country', 'POLAND (Warsaw)')
    return JsonResponse({'predictions': TRACKER.predict_passes(country)})

@csrf_exempt
def log_satellite(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'logged'})
    return JsonResponse({'status': 'error'})
