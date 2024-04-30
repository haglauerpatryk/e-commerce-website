from django.views import generic

class BlogView(generic.TemplateView):
    """
    Website home page.

    **Template:**

    :template:`blog/blog.html`
    """
    template_name = "blog/blog.html"