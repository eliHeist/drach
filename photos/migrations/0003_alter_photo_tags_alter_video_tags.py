# Generated by Django 4.0.4 on 2022-05-11 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_tags_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='photos', to='photos.tag'),
        ),
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='videos', to='photos.tag'),
        ),
    ]
