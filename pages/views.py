from django.shortcuts import render
from django.views import View
import datetime


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'year': datetime.datetime.now().year
        }
        return render(request, 'pages/home.html', context)
