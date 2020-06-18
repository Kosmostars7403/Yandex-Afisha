from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from places.models import Place, Image
import json

def index(request):
    template = loader.get_template('index.html')
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
                "detailsUrl": '/places/{}'.format(place.pk)
            }
        }
        context['places_geojson']['features'].append(place_geo)

    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)

def places(request,place_id):
    place = get_object_or_404(Place, id=place_id)
    response_data = {
    "title": place.title,
    "imgs": [
        image_link.get_absolute_image_url() for image_link in Image.objects.filter(place__id=place_id)
    ],
    "description_short": place.description_short,
    "description_long": place.description_long,
    "coordinates": {
        "lat": place.lat,
        "lng": place.lng
    }
    }
    return HttpResponse(json.dumps(response_data, ensure_ascii=False, indent=4),
                        content_type="application/json")



