# Django
from django.urls import path

# Internal
from math_challenge.views import LeastCommonMultipleViews, ServicesPlusOneViews

urlpatterns = [
    path(
        'least_commin_multiple/',
        LeastCommonMultipleViews.as_view(),
        name='least_commin_multiple'
    ),
    path(
        'plus_one/',
        ServicesPlusOneViews.as_view(),
        name='plus_one'
    )
]