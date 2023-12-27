from django.shortcuts import render
from django.views.generic import ListView

from main.models import Newsletter


# Create your views here.


class NewsletterListView(ListView):
    model = Newsletter