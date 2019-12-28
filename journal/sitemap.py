from django.contrib.sitemaps import Sitemap
from .models import Paper
from django.urls import reverse
from django.contrib import sitemaps

 
 
class PaperSitemap(Sitemap):    
    changefreq = "daily"
    priority = 0.5
 
    def items(self):
        return Paper.objects.all()
 
    def location(self, item):
        return reverse('abstract_detail', args=[item.slug])



class StaticSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'about', 'contact']

    def location(self, item):
        return reverse(item)