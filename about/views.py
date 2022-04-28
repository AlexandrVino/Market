from django.views.generic.base import TemplateView

ABOUT_TEMPLATE = "about/description.html"


class DescriptionView(TemplateView):
    """Возвращает страничку информации о проекте"""

    template_name = ABOUT_TEMPLATE
