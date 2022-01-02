from django.core.paginator import Paginator
from django.conf import settings


def get_page_context(queryset, request):
    paginator = Paginator(queryset, settings.PAGE_SITE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {
        'page_obj': page_obj,
    }
