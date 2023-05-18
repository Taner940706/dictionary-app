from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic as views


@login_required
class Home(views.ListView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




