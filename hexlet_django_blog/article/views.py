from django.http import HttpResponse
from django.views import View

class Index(View):
    def get(self, request):
        return HttpResponse('article', context={'name': 'article'})
