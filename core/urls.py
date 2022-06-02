from django.urls import path
from .views import sections

urlpatterns = [
    path('sections/get_all', sections.get_all, name="get_all_sections"),
]
