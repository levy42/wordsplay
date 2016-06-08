from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
class HomeView(TemplateView):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        context = {
            'some_dynamic_value': 'This text comes from django view!',
        }
        return self.render_to_response(context)

@login_required
def test(request):
    return HttpResponse('aergbregreg', status=201)
