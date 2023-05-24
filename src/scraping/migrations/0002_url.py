# Generated by Django 3.0.8 on 2023-05-22 16:50

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import scraping.models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_data', jsonfield.fields.JSONField(default=scraping.models.default_urls)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.City', verbose_name='Город')),
                ('metro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.Metro', verbose_name='Метро')),
            ],
            options={
                'unique_together': {('city', 'metro')},
            },
        ),
    ]
