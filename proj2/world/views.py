from django.http import HttpResponse
import logging
# Create your views here.

logger = logging.getLogger(__name__)


def index(request, *args, **kwargs):
    logger.info('We are the in world app')
    return HttpResponse('WORLD')
