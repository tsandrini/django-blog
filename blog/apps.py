from django.apps import AppConfig
from django.utils.translation import ugettext as _


class BlogConfig(AppConfig):
    name = 'tsandrini.blog'
    verbose_name = _("django blog module")
