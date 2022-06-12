from django.urls import path
from .views import main_page,blog_post,topic_page
from django.contrib.sitemaps.views import sitemap
from .sitemaps import Static_Sitemap,Article_Sitemap,Topic_Sitemap

sitemaps = {
    'article':Article_Sitemap(),
    "static":Static_Sitemap(), 
    "topic":Topic_Sitemap()
}

print(sitemaps)

urlpatterns = [
    path('', main_page, name='blog_list'),
    path('blog/<slug>',blog_post ,name="blog_post"),
    path('topic/<topic>',topic_page,name="blog_topic"),
    path(r'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]


# handler404 = 'blog.views.handler404'