# Generated by Django 3.0.4 on 2021-08-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='name',
            field=models.CharField(blank=True, default='', max_length=999, null=True),
        ),
    ]
