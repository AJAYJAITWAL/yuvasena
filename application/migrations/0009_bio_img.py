# Generated by Django 3.0.2 on 2020-08-30 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20200827_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='img',
            field=models.ImageField(default=True, upload_to=''),
            preserve_default=False,
        ),
    ]
