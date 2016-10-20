from django.shortcuts import render
from django.http import HttpResponse
import logging
# Create your views here.

logger = logging.getLogger(__name__)

def index(request, *args, **kwargs):
    logger.info('We are the in hello app')
    return HttpResponse('HELLO')
