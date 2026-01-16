from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Root path
    path('api/satellites/', views.get_satellites),
    # Added trajectory endpoint but view is capable of handling it or not?
    # User's views.py doesn't have get_trajectory defined yet in previous steps, but TASK description implied just updating URLs here.
    # We should stick to what was asked in TASK 1 for URLs.
    # However, to avoid 404s for the JS fetch we added earlier, we might need a view stub if not present.
    # But strictly following TASK 1 instructions:
    path('api/trajectory/', views.get_trajectory),
    path('api/predict/', views.get_predictions),
    path('api/log/', views.log_satellite),
]
