# Generated by Django 2.2.5 on 2019-09-28 14:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact_us',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contact_us',
            name='statut',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsletter',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='statut',
            field=models.BooleanField(default=True),
        ),
    ]