# Generated by Django 3.0.7 on 2020-06-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_image_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]