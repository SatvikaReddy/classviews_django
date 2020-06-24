from django.views.generic import TemplateView
from django.shortcuts import render

class HomeView(TemplateView):
    var1 = 'This is variable 1'
    var2 = 'This is variable 2'

    def get(self, request, *args, **kwargs):
        context = locals()
        context['var1'] = self.var1
        context['var2'] = self.var2
        return render(request, "home.html" ,context)