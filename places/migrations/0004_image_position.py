# Generated by Django 3.0.7 on 2020-06-18 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20200618_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Позиция'),
            preserve_default=False,
        ),
    ]
