# Generated by Django 3.0.2 on 2020-08-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='content',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default=2, max_length=225),
            preserve_default=False,
        ),
    ]