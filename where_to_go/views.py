from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from places.models import Place, Image
from django.urls import reverse
import json
from django.shortcuts import render

def index(request):
    places = Place.objects.all()
    context = {'places_geojson':
        {
        "type": "FeatureCollection",
        "features": []
        }
    }
    for place in places:
        place_geo = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.pk,
                "detailsUrl": reverse('places', args=[place.pk])
            }
        }
        context['places_geojson']['features'].append(place_geo)

    return render(request, 'index.html', context=context)


def places(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    response_data = {
        "title": place.title,
        "imgs": [
            image.file.url for image in place.place_images.all()
        ],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng
        }
    }
    return JsonResponse(response_data)



