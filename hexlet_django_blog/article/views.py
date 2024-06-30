from django.http import HttpResponse

def index(request):
    return HttpResponse('article', context={'name': 'article'})
