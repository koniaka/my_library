# Generated by Django 3.0.5 on 2020-04-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20200406_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishing',
            name='sity',
            field=models.CharField(default=True, max_length=20),
            preserve_default=False,
        ),
    ]
