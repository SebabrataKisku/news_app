from django.contrib import admin

from articles.models import Article
from .models import Article

admin.site.register(Article)