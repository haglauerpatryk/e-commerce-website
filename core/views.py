from django.views import generic

class IndexView(generic.TemplateView):
    """
    Website home page.

    **Template:**

    :template:`core/index.html`
    """
    template_name = "core/index.html"

class AboutView(generic.TemplateView):
    """
    About page.

    **Template:**

    :template:`core/about.html`
    """
    template_name = "core/about.html"

class ContactView(generic.TemplateView):
    """
    Contact page.

    **Template:**

    :template:`core/contact.html`
    """
    template_name = "core/contact.html"