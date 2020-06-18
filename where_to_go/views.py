from django.http import HttpResponse
from django.template import loader
from places.models import Place, Image

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
                "placeId": "moscow_legends",
                "detailsUrl": "{% static 'places/moscow_legends.json' %}"
            }
        }
        context['places_geojson']['features'].append(place_geo)

    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)