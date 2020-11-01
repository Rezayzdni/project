# Generated by Django 3.1.2 on 2020-10-07 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', stdimage.models.StdImageField(blank=True, default='default.jpg', upload_to='profile_pics')),
                ('currentLocation', models.CharField(blank=True, default='-', max_length=25)),
                ('phoneNumber', models.CharField(blank=True, default='-', max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]