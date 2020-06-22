from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image
import requests
from PIL import Image as Image_PIL
from io import BytesIO
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Добавляет место в БД по ссылке'

    def add_arguments(self, parser):
        parser.add_argument('url')

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status
        response = response.json()

        place = Place.objects.create(title=response['title'], description_short=response['description_short'],
                            description_long=response['description_long'], lng=response['coordinates']['lng'],
                            lat=response['coordinates']['lat'])

        for image_link in response['imgs']:
            response = requests.get(image_link)
            imagefile = ContentFile(response.content)
            filename = image_link.split('/')[-1]

            image = Image.objects.create(place=place)
            image.file.save(filename, imagefile, save=True)
