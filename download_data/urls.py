from django.urls import path

from download_data.views import download_sentinal_data

urlpatterns = [
    path('sentinal/', download_sentinal_data, name='download_sentinal_data')
]
