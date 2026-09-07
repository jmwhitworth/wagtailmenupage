from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WagtailmenupageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wagtailmenupage"
    verbose_name = _("Wagtail Menu Page")
