from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from posts.models import Article

def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'article_detail.html', {'article': article})
