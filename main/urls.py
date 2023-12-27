from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import NewsletterListView

app_name = MainConfig.name

urlpatterns = [
    path('', NewsletterListView.as_view(), name='home'),
]