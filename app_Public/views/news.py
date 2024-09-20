from django.views.generic import TemplateView
class NewsView(TemplateView):
    template_name = "public/pages/news.html"