from django.urls import path
from . views import JobsView

urlpatterns = [
    path('jobs/', JobsView.as_view(), name='jobs_view'),
]