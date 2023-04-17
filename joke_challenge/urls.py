# Django
from django.urls import path

# Internal
from joke_challenge.views import JokeChallengeViews

urlpatterns = [
    path(
        'joke/',
        JokeChallengeViews.as_view(),
        name='joke'
    ),    
]