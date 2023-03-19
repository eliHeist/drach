# Generated by Django 4.0.4 on 2022-05-23 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventimage',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='events.event'),
        ),
        migrations.AlterField(
            model_name='eventvideo',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='events.event'),
        ),
    ]