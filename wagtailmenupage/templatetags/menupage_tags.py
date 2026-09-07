from typing import Optional

from django import template
from wagtail.models import Site

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context, *args, **kwargs) -> Optional[Site]:
    if request := context.get("request"):
        return Site.find_for_request(request).root_page
    return None
