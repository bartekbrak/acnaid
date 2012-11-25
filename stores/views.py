from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.localflavor.pl import pl_voivodeships
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.core import serializers
from models import *

# voivodeship slug
STORES_DEFAULT_VOIVODESHIP = getattr(settings, 'STORES_DEFAULT_VOIVODESHIP',
                                     'masovia')

# voivodeship slug
STORES_DEFAULT_LOCALITY = getattr(settings, 'STORES_DEFAULT_LOCALITY',
                                  ('warszawa', "Warszawa"))


def index(request):
    voivodeships = dict(pl_voivodeships.VOIVODESHIP_CHOICES)
    localities = Locality.objects.filter(
        voivodeship=STORES_DEFAULT_VOIVODESHIP
    ).order_by('name')
    return render_to_response('stores/index.html', {
        'voivodeships': voivodeships,
        'localities': localities,
        'default_locality': STORES_DEFAULT_LOCALITY,
        'current_voivodeship': STORES_DEFAULT_VOIVODESHIP,
        'current_voivodeship_name': voivodeships[STORES_DEFAULT_VOIVODESHIP],
    }, context_instance=RequestContext(request))


def get_localities(request):
    if not request.method == 'GET' or not 'slug' in request.GET or not request.is_ajax():
        return HttpResponseBadRequest()
    slug = request.GET.get('slug')
    try:
        localities = Locality.objects.filter(voivodeship=slug).order_by('name')
    except:
        return HttpResponseNotFound()
    return HttpResponse(serializers.serialize('json', localities), mimetype='application/json')


def get_stores(request):
    if not request.method == 'GET' or not 'slug' in request.GET or not 'voivodeship' in request.GET or not request.is_ajax():
        return HttpResponseBadRequest('1')
    slug = request.GET.get('slug')
    voivodeship = request.GET.get('voivodeship')
    try:
        stores = Store.objects.filter(locality__slug=slug, locality__voivodeship=voivodeship).order_by('address')
    except:
        return HttpResponseNotFound()
    return HttpResponse(serializers.serialize('json', stores), mimetype='application/json')
