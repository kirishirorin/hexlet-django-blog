from django.http import HttpResponse
from django.views import View

class Index(View):
    def get(self, request):
        return reverse('article', kwargs={'tags': python, 'article_id': 42})

def med_info_view(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
