# from django.shortcuts import render
#
#
# def index_page(request):
#     return render(request, 'home.html')
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'
 # class AboutPageView(TemplateView):
 #     template_name = '.html'