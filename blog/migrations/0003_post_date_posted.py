# Generated by Django 3.1.2 on 2020-10-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201011_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]