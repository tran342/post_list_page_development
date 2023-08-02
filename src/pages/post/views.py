from django.views.generic import TemplateView


class PostView(TemplateView):
    template_name = "pages/post/index.html"


class PostDetailView(TemplateView):
    template_name = "pages/post/detail.html"
